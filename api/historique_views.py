from django.db.models import Q

from rest_framework import (
    filters,
    generics,
    status,
)
from rest_framework.response import Response

from .models import Historique
from .pagination import HistoriquePagination
from .serializers import HistoriqueSerializer


class HistoriqueListView(generics.ListAPIView):

    serializer_class = HistoriqueSerializer
    pagination_class = HistoriquePagination

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
        Retourne exclusivement un QuerySet.
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
                annee_concours=annee_concours,
            )

        if (
            type_session
            and type_session.lower() != "all"
        ):
            queryset = queryset.filter(
                type_session__iexact=type_session,
            )

        return queryset

    def list(self, request, *args, **kwargs):
        """
        Applique les filtres, la recherche,
        le tri et la pagination.
        """

        queryset = self.filter_queryset(
            self.get_queryset()
        )

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(
                page,
                many=True,
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
                        "count": (
                            self.paginator.page
                            .paginator.count
                        ),
                        "next": (
                            self.paginator
                            .get_next_link()
                        ),
                        "previous": (
                            self.paginator
                            .get_previous_link()
                        ),
                        "results": serializer.data,
                    },
                },
                status=status.HTTP_200_OK,
            )

        serializer = self.get_serializer(
            queryset,
            many=True,
        )

        return Response(
            {
                "code": status.HTTP_200_OK,
                "success": True,
                "message": (
                    "Liste des historiques récupérée "
                    "avec succès."
                ),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )