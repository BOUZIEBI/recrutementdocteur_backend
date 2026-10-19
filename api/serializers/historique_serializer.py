from rest_framework import serializers
from api.models import Historique


class HistoriqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Historique
        fields = "__all__"
        read_only_fields = ["uid"]
        
        # Ne jamais retourner le mot de passe.
        exclude = [
            "password",
        ]