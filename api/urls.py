from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView


from api.views import ImportHistoriqueAPIView
from api.views.historique_views import HistoriqueListView
from .auth_views import (
    RegisterView,
    LoginView,
    GetMeView,
    LogoutView,
)


urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/me/", GetMeView.as_view(), name="get_me"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("historiques/import-excel/",ImportHistoriqueAPIView.as_view(),name="import-historiques-excel"),
    path(
        "historiques/",
        HistoriqueListView.as_view(),
        name="historique-list",
    ),
    
]