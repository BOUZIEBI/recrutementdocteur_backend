from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password
from .models import Candidat, Historique, Role

User = get_user_model()


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = [
            "uid",
            "libelle",
            "code",
        ]


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = [
            "id",
            "codename",
            "name",
        ]



class CandidatSerializer(serializers.ModelSerializer):

    genre_libelle = serializers.CharField(
        source="get_genre_display",
        read_only=True
    )

    class Meta:
        model = Candidat

        fields = [
            "uid",
            "password",
            "email",
            "nom",
            "prenoms",
            "numero_candidat",
            "matricule",
            "code",
            "date_naissance",
            "lieu_naissance",
            "telephone_principal",
            "telephone_secondaire",
            "email_professionnel",
            "email_personnel",
            "nom_jeune_fille",
            "lieu_habitation",
            "date_recrutement",
            "nombre_enfant",
            "numero_piece_identite",
            "date_obtention_diplome",
            "cree_le",
            "modifie_le",
            "preinscrit_le",
            "supprime_le",
            "date_premiere_prise_service_dans_structure",
            "date_premiere_prise_service_fonction_publique",

            # États
            "etat_handicap",
            "is_mode",
            "is_deleted",
            "est_inscrit",

            # Utilisateurs
            "cree_par",
            "modifie_par",
            "supprime_par",

            # Relations
            "diplome",
            "institution_dorigine",
            "genre",
            "genre_libelle",
            "nationalite",
            "type_recrutement",
            "structure",
            "situation_matrimoniale",
            "situation_administrative",
            "grade",
            "pays_residence",
            "pays_obtention",
            "nombre_publication",
            "user",
        ]

        read_only_fields = [
            "uid",
            "cree_le",
            "modifie_le",
            "supprime_le",
            "cree_par",
            "modifie_par",
            "supprime_par",
            "is_deleted",
        ]

        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": False,
                "allow_blank": False,
                "trim_whitespace": False,
                "style": {"input_type": "password"},
            },
            "email": {
                "required": False,
                "allow_null": True,
                "allow_blank": True,
            },
        }

    def validate_email(self, value):
        if value:
            return serializers.EmailField().run_validation(value)
        return value

    def validate_nombre_enfant(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Le nombre d'enfants ne peut pas être négatif."
            )
        return value

    def create(self, validated_data):
        password = validated_data.pop("password", None)

        candidat = Candidat(**validated_data)

        if password:
            candidat.password = make_password(password)
        else:
            candidat.password = make_password(None)

        candidat.save()
        return candidat

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.password = make_password(password)

        instance.save()
        return instance
        

class UserSerializer(serializers.ModelSerializer):

    role = RoleSerializer(
        read_only=True
    )

    permissions = serializers.SerializerMethodField()

    candidat = CandidatSerializer(
        read_only=True,
        allow_null=True
    )

    class Meta:
        model = User

        fields = [
            "uid",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_verified",
            "role",
            "permissions",
            "candidat",
            "candidat",
            "cree_le",
            "modifie_le",
        ]

        read_only_fields = fields

    def get_permissions(self, obj):

        permissions = obj.user_permissions.all()

        return PermissionSerializer(
            permissions,
            many=True
        ).data


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    password_confirm = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User

        fields = [
            "uid",
            "username",
            "email",
            "password",
            "password_confirm",
        ]

        read_only_fields = ["uid"]

    def validate(self, attrs):

        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError({
                "password_confirm": "Les mots de passe ne correspondent pas."
            })

        return attrs

    def validate_email(self, value):

        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(
                "Cette adresse email est déjà utilisée."
            )

        return value

    def create(self, validated_data):

        validated_data.pop("password_confirm")

        password = validated_data.pop("password")

        user = User(**validated_data)

        user.set_password(password)

        # À adapter selon ton processus d'activation.
        user.is_active = True
        user.is_verified = True
        
        # Dates
        current_time = timezone.now()

        user.cree_le = current_time
        user.modifie_le = current_time

        user.save()

        return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True
    )


class LogoutSerializer(serializers.Serializer):

    refresh_token = serializers.CharField(
        required=True
    )
    
    
class ImportHistoriqueSerializer(serializers.Serializer):

    fichier = serializers.FileField(
        required=True
    )

    annee_concours = serializers.CharField(
        max_length=50,
        required=True
    )

    type_session = serializers.CharField(
        max_length=30,
        required=True
    )
    
    def validate_fichier(self, fichier):

        extensions = (".xls", ".xlsx")

        if not fichier.name.lower().endswith(extensions):
            raise serializers.ValidationError(
                "Le fichier doit être au format .xls ou .xlsx."
            )

        if fichier.size > 10 * 1024 * 1024:
            raise serializers.ValidationError(
                "La taille maximale autorisée est de 10 Mo."
            )

        return fichier


class HistoriqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Historique
        fields = "__all__"
        read_only_fields = ["uid"]