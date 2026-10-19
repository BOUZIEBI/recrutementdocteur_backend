from django.conf import settings
from django.db import models
import uuid
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class StatutCandidature(models.TextChoices):
    EN_ATTENTE = "EN_ATTENTE", "En attente"
    ACCEPTEE = "ACCEPTEE", "Acceptée"
    REJETEE = "REJETEE", "Rejetée"
    ANNULEE = "ANNULEE", "Annulée"
    
    
class Genre(models.TextChoices):
    MASCULIN = "H", "Masculin"
    FEMININ = "F", "Feminin"


class StatutPaiementEnum(models.TextChoices):
    EN_ATTENTE = "EN_ATTENTE", "En attente"
    EN_COURS = "EN_COURS", "En cours"
    REUSSI = "REUSSI", "Réussi"
    ECHOUE = "ECHOUE", "Échoué"
    ANNULE = "ANNULE", "Annulé"
    REMBOURSE = "REMBOURSE", "Remboursé"


class ModePaiementEnum(models.TextChoices):
    ORANGE_MONEY = "ORANGE_MONEY", "Orange Money"
    MTN_MONEY = "MTN_MONEY", "MTN Mobile Money"
    MOOV_MONEY = "MOOV_MONEY", "Moov Money"
    WAVE = "WAVE", "Wave"
    CARTE_BANCAIRE = "CARTE_BANCAIRE", "Carte bancaire"
    VIREMENT = "VIREMENT", "Virement bancaire"
    ESPECES = "ESPECES", "Espèces"
    
    
class TypeStructure(models.TextChoices):
    UNIVERSITE = "UNIVERSITE", "Université"
    AUTRE = "AUTRE", "Autre"
    
class TypeSession(models.TextChoices):
    SESSIONANNEE = "SESSIONANNEE", "Session de l'année"
    SESSIONCOMPLEMENTAIRE = "SESSIONCOMPLEMENTAIRE", "Session complementaire"
    
    

class Handicap(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    modifie_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "handicaps"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class TypeRecrutement(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    modifie_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "type_recrutements"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class Pays(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    modifie_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "pays"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class Ville(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "villes"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class Diplome(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "diplomes"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    
    

class Structure(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )
    
    type_structure = models.CharField(
        max_length=20,
        choices=TypeStructure.choices,
        default=TypeStructure.UNIVERSITE
    )

    class Meta:
        db_table = "structures"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class InstitutionDorigine(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "institution_dorigines"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    
    

class Discipline(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "disciplines"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    


class Specialite(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "specialites"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class Role(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "roles"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class User(AbstractUser):

    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    is_verified = models.BooleanField(
        null=True,
        blank=True,
        default=None
    )
    is_active = models.BooleanField(
        null=True,
        blank=True,
        default=None
    )
    is_superuser = models.BooleanField(
        null=True,
        blank=True,
        default=None
    )
    
    # Dates
    cree_le = models.DateTimeField(
        null=True,
        blank=True
    )

    modifie_le = models.DateTimeField(
        null=True,
        blank=True
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True
    )
    
    # Relation avec Role
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
        db_column="role_uid"
    )

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username



class Statut(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )
 
    class Meta:
        db_table = "statuts" 
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)


class Grade(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )
 
    class Meta:
        db_table = "grades" 
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class SituationAdministrative(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    ) 
 
    class Meta:
        db_table = "situation_administratives" 
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    
    

class Domaine(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "domaines"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class SituationMatrimoniale(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "situation_matrimoniales" 
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class Fonction(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "fonctions"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class TypeStructure(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        null=True,
        blank=True
    )

    modifie_le = models.DateTimeField(
        null=True,
        blank=True
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "type_structures"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    

class Conjoint(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    nom = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    prenoms = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    matricule_cnps = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    profession = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    cree_le = models.DateTimeField(
        null=True,
        blank=True
    )

    modifie_le = models.DateTimeField(
        null=True,
        blank=True
    )

    is_mode = models.BooleanField(
        default=None,
        null=True,
        blank=True
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = "conjoints"
        verbose_name = "Conjoint"
        verbose_name_plural = "Conjoints"

    def __str__(self):
        return f"{self.nom or ''} {self.prenoms or ''}".strip()
    
    

class Nationalite(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "nationalites"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    
    
    
    
class NaturePieceidentite(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    libelle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modifie_le = models.DateTimeField(
        auto_now=True,
    )

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=True,
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "natures_piece_identite"
        ordering = ["libelle"]

    def __str__(self) -> str:
        return self.libelle or self.code or str(self.uid)
    


class Candidat(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    password = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    email = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    nom = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    prenoms = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    numero_candidat = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    
    matricule = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    code = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    date_naissance = models.DateTimeField(
        null=True,
        blank=True
    )

    lieu_naissance = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    annee_concours = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    telephone_principal = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    telephone_secondaire = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    email_professionnel = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    email_personnel = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    nom_jeune_fille = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    lieu_habitation = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    date_recrutement = models.DateTimeField(
        null=True,
        blank=True
    )

    nombre_enfant = models.IntegerField(
        default=0
    )


    numero_piece_identite = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    
    date_obtention_diplome = models.DateTimeField(
        null=True,
        blank=True
    )
    
    cree_le = models.DateTimeField(
        null=True,
        blank=True
    )

    modifie_le = models.DateTimeField(
        null=True,
        blank=True
    )

    preinscrit_le = models.DateTimeField(
        null=True,
        blank=True
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True
    )

    date_premiere_prise_service_dans_structure = (
        models.DateTimeField(
            null=True,
            blank=True
        )
    )

    date_premiere_prise_service_fonction_publique = (
        models.DateTimeField(
            null=True,
            blank=True
        )
    )

    # ==========================================
    # ETATS
    # ==========================================

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=None
    )

    is_deleted = models.BooleanField(
        null=True,
        blank=True,
        default=None
    )

    est_inscrit = models.BooleanField(
        null=True,
        blank=True,
        default=None
    )

    # ==========================================
    # UTILISATEURS
    # ==========================================

    cree_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidat_cree_par",
        db_column="cree_par_uid"
    )

    modifie_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidat_modifie_par",
        db_column="modifie_par_uid"
    )

    supprime_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidat_supprime_par",
        db_column="supprime_par_uid"
    )

    # ==========================================
    # RELATIONS
    # ==========================================
    handicap = models.ForeignKey(
        Handicap,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_handicap",
        db_column="handicap_uid"
    )
    diplome = models.ForeignKey(
        Diplome,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_diplome",
        db_column="diplome_uid"
    )
    institution_dorigine = models.ForeignKey(
        InstitutionDorigine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_institution_dorigines",
        db_column="instition_dorigine_uid"
    )
    genre = models.CharField(
        max_length=20,
        choices=Genre.choices,
        default=Genre.MASCULIN
    )
    type_session = models.CharField(
        max_length=225,
        choices=TypeSession.choices,
        default=TypeSession.SESSIONANNEE
    )
    nationalite = models.ForeignKey(
        Nationalite,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_nationalite",
        db_column="nationalite_uid"
    )

    type_recrutement = models.ForeignKey(
        TypeRecrutement,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_type_recrutement",
        db_column="type_recrutement_uid"
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_structure",
        db_column="structure_uid"
    )

    situation_matrimoniale = models.ForeignKey(
        SituationMatrimoniale,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_situation_matrimoniale",
        db_column="situation_matrimoniale_uid"
    )

    
    situation_administrative = models.ForeignKey(
        SituationAdministrative,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_situation_administrative",
        db_column="situation_administrative_uid"
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_grade",
        db_column="grade_uid"
    )
    
    pays_residence = models.ForeignKey(
        Pays,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_pays_residence",
        db_column="pays_residence_uid"
    )
    
    pays_obtention = models.ForeignKey(
        Pays,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_diplome_pays_obtention",
        db_column="pays_obtention_uid"
    )
    
    nombre_publication= models.PositiveIntegerField(
        null=True,
        blank=True
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="candidats_user",
        db_column="user_uid"
    )

    # ==========================================
    # CONFIGURATION
    # ==========================================

    class Meta:
        db_table = "candidats"
        ordering = ["nom", "prenoms"]
        verbose_name = "Candidat"
        verbose_name_plural = "Candidats"

    def __str__(self):
        return f"{self.nom or ''} {self.prenoms or ''}".strip()
    
    
class Historique(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    password = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    email = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    nom_prenoms = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    numero_candidat = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    
    matricule = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    code = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    annee_concours = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    date_naissance = models.DateTimeField(
        null=True,
        blank=True
    )

    lieu_naissance = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    telephone = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    email_professionnel = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    email_personnel = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    nom_jeune_fille = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    lieu_habitation = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    date_recrutement = models.DateTimeField(
        null=True,
        blank=True
    )

    nombre_enfant = models.IntegerField(
        default=0
    )


    numero_piece_identite = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    
    date_obtention_diplome = models.DateTimeField(
        null=True,
        blank=True
    )
    
    cree_le = models.DateTimeField(
        null=True,
        blank=True
    )

    modifie_le = models.DateTimeField(
        null=True,
        blank=True
    )

    preinscrit_le = models.DateTimeField(
        null=True,
        blank=True
    )

    supprime_le = models.DateTimeField(
        null=True,
        blank=True
    )

    date_premiere_prise_service_dans_structure = (
        models.DateTimeField(
            null=True,
            blank=True
        )
    )

    date_premiere_prise_service_fonction_publique = (
        models.DateTimeField(
            null=True,
            blank=True
        )
    )

    # ==========================================
    # ETATS
    # ==========================================

    is_mode = models.BooleanField(
        null=True,
        blank=True,
        default=None
    )

    is_deleted = models.BooleanField(
        null=True,
        blank=True,
        default=None
    )

    est_inscrit = models.BooleanField(
        null=True,
        blank=True,
        default=None
    )

    # ==========================================
    # UTILISATEURS
    # ==========================================

    cree_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_cree_par",
        db_column="cree_par_uid"
    )

    modifie_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_modifie_par",
        db_column="modifie_par_uid"
    )

    supprime_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_upprime_par",
        db_column="supprime_par_uid"
    )

    # ==========================================
    # RELATIONS
    # ==========================================
    handicap = models.ForeignKey(
        Handicap,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_handicap",
        db_column="handicap_uid"
    )
    diplome = models.ForeignKey(
        Diplome,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_diplome",
        db_column="diplome_uid"
    )
    institution_dorigine = models.ForeignKey(
        InstitutionDorigine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_institution_dorigines",
        db_column="instition_dorigine_uid"
    )
    genre = models.CharField(
        max_length=20,
        choices=Genre.choices,
        default=Genre.MASCULIN,
        null=True,
        blank=True,
    )
    type_session = models.CharField(
        max_length=225,
        choices=TypeSession.choices,
        default=TypeSession.SESSIONANNEE
    )
    nationalite = models.ForeignKey(
        Nationalite,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_nationalite",
        db_column="nationalite_uid"
    )

    type_recrutement = models.ForeignKey(
        TypeRecrutement,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_type_recrutement",
        db_column="type_recrutement_uid"
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_structure",
        db_column="structure_uid"
    )

    situation_matrimoniale = models.ForeignKey(
        SituationMatrimoniale,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_situation_matrimoniale",
        db_column="situation_matrimoniale_uid"
    )

    
    situation_administrative = models.ForeignKey(
        SituationAdministrative,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_situation_administrative",
        db_column="situation_administrative_uid"
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_grade",
        db_column="grade_uid"
    )
    
    pays_residence = models.ForeignKey(
        Pays,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_pays_residence",
        db_column="pays_residence_uid"
    )
    
    pays_obtention = models.ForeignKey(
        Pays,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_diplome_pays_obtention",
        db_column="pays_obtention_uid"
    )
    
    nombre_publication= models.PositiveIntegerField(
        null=True,
        blank=True
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historiques_user",
        db_column="user_uid"
    )

    # ==========================================
    # CONFIGURATION
    # ==========================================

    class Meta:
        db_table = "historiques"
        ordering = ["nom_prenoms"]
        verbose_name = "Historique"
        verbose_name_plural = "Historiques"
        
        

    def __str__(self):
        return f"{self.nom_prenoms}"
    
    
class Postulation(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    code = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    domaine = models.ForeignKey(
        Domaine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="domaines",
        db_column="domaine_uid"
    )
    
    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="postulations_discipline",
        db_column="discipline_uid"
    )

    specialite = models.ForeignKey(
        Specialite,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="postulations_specialite",
        db_column="specialite_uid"
    )
    
    candidat = models.ForeignKey(
        Candidat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="postulations_candidat",
        db_column="candidat_uid"
    )
    
    date_postulation = models.DateTimeField(
        null=True,
        blank=True
    )
    
    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    modifie_le = models.DateTimeField(
        auto_now=True
    )
        
    class Meta:
        db_table = "postulations"
        verbose_name = "Postulation"
        verbose_name_plural = "Postulations"
        ordering = ["-cree_le"]
        
    def __str__(self) -> str:
        return self.code or str(self.uid)


class Paiement(models.Model):

    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    candidat = models.ForeignKey(
        Candidat,
        on_delete=models.PROTECT,
        related_name="paiements"
    )

    reference = models.CharField(
        max_length=100,
        unique=True
    )

    reference_transaction = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        db_index=True
    )

    montant = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    devise = models.CharField(
        max_length=3,
        default="XOF"
    )

    mode_paiement = models.CharField(
        max_length=30,
        choices=ModePaiementEnum.choices
    )

    statut = models.CharField(
        max_length=20,
        choices=StatutPaiementEnum.choices,
        default=StatutPaiementEnum.EN_ATTENTE
    )

    numero_telephone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    operateur = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    date_paiement = models.DateTimeField(
        null=True,
        blank=True
    )

    date_confirmation = models.DateTimeField(
        null=True,
        blank=True
    )

    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    modifie_le = models.DateTimeField(
        auto_now=True
    )
    
    postulation = models.ForeignKey(
        Postulation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="paiements_postulation",
        db_column="postulation_uid"
    )

    class Meta:
        db_table = "paiements"
        ordering = ["-cree_le"]
        indexes = [
            models.Index(fields=["candidat", "statut"]),
            models.Index(fields=["cree_le"]),
        ]

    def __str__(self):
        return f"{self.reference} - {self.montant} {self.devise}"
    
    
class ResultatConcours(models.Model):

    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    moyenne = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    
    classement= models.PositiveIntegerField(
        null=True,
        blank=True
    )
    
    avis_cnres = models.TextField(
        null=True,
        blank=True
    )
    
    observation = models.TextField(
        null=True,
        blank=True
    )
    
    candidat = models.ForeignKey(
        Candidat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="resultatconcours_candidat",
        db_column="candidat_uid"
    )
    
    cree_le = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    modifie_le = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "resultat_concours"
        ordering = ["cree_le"]

    def __str__(self):
        return f"{self.classement}"
        