from django.contrib.auth import authenticate, get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework import status
from rest_framework.response import Response
from .serializers import (
    UserSerializer,
    RegisterSerializer,
    LoginSerializer,
    LogoutSerializer,
)


User = get_user_model()


def generate_tokens(user):

    refresh = RefreshToken.for_user(user)

    return {
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh),
        "token_type": "Bearer",
        "expires_in": 30 * 60,
    }


class CustomJWTAuthentication(JWTAuthentication):

    def get_validated_token(self, raw_token):
        try:
            return super().get_validated_token(raw_token)

        except InvalidToken as exc: 
            return Response({
                "code": 401,
                "success": False,
                "message": "Le token est expiré ou invalide.",
                "error_code": "TOKEN_INVALID_OR_EXPIRED",
            }, status=status.HTTP_200_OK)
            

# ----------------------------------------
# REGISTER
# ----------------------------------------

class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        if not serializer.is_valid():

            return Response({
                "code": 400,
                "success": False,
                "message": "Erreur de validation.",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()

        return Response({
            "code": 201,
            "success": True,
            "message": "Utilisateur enregistré avec succès.",
            "data": UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)


# ----------------------------------------
# LOGIN
# ----------------------------------------

class LoginView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        print("LoginView: username:", username, "password:", password)  # Debugging line
        user = authenticate(
            request=request,
            username=username,
            password=password
        )
       
        if user is None:

            return Response({
                "code": status.HTTP_401_UNAUTHORIZED,
                "success": False,
                "message": "Identifiants incorrects ou compte inactif.",
                "data": None
            }, status=status.HTTP_200_OK)


        if not user.is_active:

            return Response({
                "code": status.HTTP_401_UNAUTHORIZED,
                "success": False,
                "message": "Votre compte est désactivé.",
                "data": None
            }, status=status.HTTP_200_OK)

        tokens = generate_tokens(user)

        return Response({
            "code": 200,
            "success": True,
            "message": "Connexion réussie.",
            "data": {
                "user": UserSerializer(user).data,
                **tokens
            }
        }, status=status.HTTP_200_OK)


# ----------------------------------------
# GET ME
# ----------------------------------------

class GetMeView(APIView):

    #authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        return Response({
            "code": 200,
            "success": True,
            "message": "Utilisateur connecté récupéré avec succès.",
            "data": UserSerializer(user).data
        }, status=status.HTTP_200_OK)


# ----------------------------------------
# LOGOUT
# ----------------------------------------

class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = LogoutSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data["refresh_token"]

        try:

            token = RefreshToken(refresh_token)

            # Empêche la révocation du token d'un autre utilisateur.
            if str(token.get("user_id")) != str(request.user.uid):
                return Response({
                    "code": 403,
                    "success": False,
                    "message": "Ce token ne correspond pas à l'utilisateur connecté."
                }, status=status.HTTP_403_FORBIDDEN)

            token.blacklist()

            return Response({
                "code": 200,
                "success": True,
                "message": "Déconnexion réussie.",
                "data": None
            }, status=status.HTTP_200_OK)

        except TokenError:

            return Response({
                "code": 400,
                "success": False,
                "message": "Refresh token invalide ou déjà révoqué."
            }, status=status.HTTP_400_BAD_REQUEST)