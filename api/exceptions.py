from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework_simplejwt.exceptions import InvalidToken


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is None:
        return None

    if isinstance(exc, (InvalidToken, AuthenticationFailed, NotAuthenticated)):

        details = str(response.data).lower()

        is_expired = (
            "expired" in details
            or "expiré" in details
        )

        response.status_code = status.HTTP_200_OK

        response.data = {
            "code": status.HTTP_401_UNAUTHORIZED,
            "success": False,
            "message": (
                "Votre session a expiré. Veuillez renouveler votre token."
                if is_expired
                else "Authentification requise ou token invalide."
            ),
            "error_code": (
                "TOKEN_EXPIRED"
                if is_expired
                else "TOKEN_INVALID"
            ),
            "data": None,
        }

    return response