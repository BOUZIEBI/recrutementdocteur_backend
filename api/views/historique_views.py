from django.db.models import Q

from rest_framework import (
    filters,
    generics,
    status,
)

from rest_framework.response import Response

from api.models import Historique
from api.serializers import HistoriqueSerializer


class HistoriqueListView(generics.ListAPIView):

    serializer_class = HistoriqueSerializer

    # Désactiver complètement la pagination
    pagination_class = None

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "numero_candidat",
        "nom_prenoms",
        "telephone",
        "email",
        "matricule",
    ]

    ordering_fields = [
        "nom_prenoms",
        "numero_candidat",
        "annee_concours",
        "cree_le",
        "modifie_le",
    ]

    ordering = [
        "nom_prenoms",
    ]

    def get_queryset(self):
        """
        Retourne tous les historiques non supprimés.

        Les filtres restent disponibles :
        - annee_concours
        - type_session
        - search
        - ordering
        """

        queryset = (
            Historique.objects
            .filter(
                Q(is_deleted=False)
                | Q(is_deleted__isnull=True)
            )
            .select_related(
                "cree_par",
                "modifie_par",
                "supprime_par",
                "handicap",
                "diplome",
                "institution_dorigine",
                "nationalite",
                "type_recrutement",
                "structure",
                "situation_matrimoniale",
                "situation_administrative",
                "grade",
                "pays_residence",
                "pays_obtention",
                "user",
            )
        )

        annee_concours = (
            self.request.query_params.get(
                "annee_concours"
            )
        )

        type_session = (
            self.request.query_params.get(
                "type_session"
            )
        )

        if annee_concours:
            queryset = queryset.filter(
                annee_concours=annee_concours
            )

        if (
            type_session
            and type_session.lower() != "all"
        ):
            queryset = queryset.filter(
                type_session__iexact=type_session
            )

        return queryset

    def list(self, request, *args, **kwargs):
        """
        Retourne tous les historiques sans pagination.

        Les filtres, la recherche et le tri
        restent actifs.
        """

        queryset = self.filter_queryset(
            self.get_queryset()
        )

        serializer = self.get_serializer(
            queryset,
            many=True
        )

        return Response(
            {
                "code": status.HTTP_200_OK,
                "success": True,
                "message": (
                    "Liste des historiques récupérée "
                    "avec succès."
                ),
                "data": {
                    "count": queryset.count(),
                    "results": serializer.data,
                },
            },
            status=status.HTTP_200_OK,
        )