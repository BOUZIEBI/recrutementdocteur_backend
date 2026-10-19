from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ImportHistoriqueSerializer
from api.services.import_historique import importer_historiques


class ImportHistoriqueAPIView(APIView):
    parser_classes = [
        MultiPartParser,
        FormParser,
    ]

    def post(self, request):
        serializer = ImportHistoriqueSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        resultat = importer_historiques(
            fichier=serializer.validated_data["fichier"],
            annee_concours=serializer.validated_data["annee_concours"],
            type_session=serializer.validated_data["type_session"],
        )

        return Response(
            {
                "code": 201,
                "success": True,
                "message": (
                    "Les historiques ont été importés "
                    "avec succès."
                ),
                "data": resultat,
            },
            status=status.HTTP_201_CREATED,
        )
