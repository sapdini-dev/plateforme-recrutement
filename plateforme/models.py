from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class utilisateur(models.Model):
    nom=models.CharField(max_length=40)
    mot_de_pass=models.CharField(max_length=40)


class Region(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Langue(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Diplome(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom





##model de l'avis de recrutement








        #en haut normal

class Annonce(models.Model):
    titre = models.CharField(max_length=200)  # Titre de l'annonce
    contenu = models.TextField()  # Contenu de l'annonce
    date_pub = models.DateTimeField(auto_now_add=True) 
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.titre

        from django.db import models

from django.db import models

class AvisRecrutement(models.Model):
    numero = models.IntegerField("N°", default=0)
    intitule = models.TextField("INTITULÉ DE L'AVIS", default='')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_exp = models.DateTimeField()
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.intitule

class OffreEmploi(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    date_exp = models.DateField()
    document = models.FileField(upload_to='documents/', null=True, blank=True)  # Ajout du champ document

    def __str__(self):
        return self.titre

    

    

    



# plateforme/models.py
from django.db import models
from django.contrib.auth.models import User  # Supposons que Candidat est lié à User ou autre



from django.db import models





        
from django.db import models

class Candidat(models.Model):
    SEXE_CHOICES = [
        ('H', 'Homme'),
        ('F', 'Femme'),
    ]

    SITUATION_MATRIMONIALE_CHOICES = [
        ('célibataire', 'Célibataire'),
        ('marié(e)', 'Marié(e)'),
        ('divorcé(e)', 'Divorcé(e)'),
        ('veuf(ve)', 'Veuf(ve)'),
    ]

    dernier_diplome = models.ForeignKey('Diplome', on_delete=models.CASCADE, null=True, blank=True)
    langue_parlee1 = models.ForeignKey('Langue', related_name='langue_parlee1', on_delete=models.SET_NULL, null=True, blank=True)
    langue_parlee2 = models.ForeignKey('Langue', related_name='langue_parlee2', on_delete=models.SET_NULL, null=True, blank=True)
    langue_parlee3 = models.ForeignKey('Langue', related_name='langue_parlee3', on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=True, blank=True)
    situation_activite = models.CharField(max_length=100)
    informatique = models.BooleanField(default=False)
    tablettes = models.BooleanField(default=False)
    enquete = models.BooleanField(default=False)

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    date_naissance = models.DateField(null=True, blank=True)
    lieu_naissance = models.CharField(max_length=100)
    situation_matrimoniale = models.CharField(max_length=50, choices=SITUATION_MATRIMONIALE_CHOICES)

    telephone_contact = models.CharField(max_length=20)
    telephone_whatsapp = models.CharField(max_length=20)
    numero_identification = models.CharField(max_length=50, unique=True)
    email = models.EmailField()

    cv = models.FileField(upload_to='cv/')
    certificat_nationalite = models.FileField(upload_to='cv/')
    lettre_motivation = models.FileField(upload_to='cv/')
    copie_legalise_bac = models.FileField(upload_to='cv/')
    copie_extrait_naissance = models.FileField(upload_to='cv/')
    certificat_domicile_ou_residence = models.FileField(upload_to='cv/')
    atestation_enquete = models.FileField(upload_to='cv/')

    def __str__(self):
        return f"{self.prenom} {self.nom}"


    
class Candidature(models.Model):
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
    offre_emploi = models.ForeignKey(OffreEmploi, on_delete=models.CASCADE)
    date_postulation = models.DateTimeField(auto_now_add=True)

    
class CandidatureOffre(models.Model):
    STATUT_CHOICES = [
        ('EN_COURS', 'En cours'),
        ('ACCEPTE', 'Accepté'),
        ('REJETE', 'Rejeté'),
    ]

    candidat = models.ForeignKey(Candidat, on_delete=models.PROTECT, related_name='candidatures')
    offre_emploi = models.ForeignKey(OffreEmploi, on_delete=models.CASCADE, related_name='candidatures')
    date_candidature = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES)

    def __str__(self):
        return f"Candidature de {self.candidat} pour {self.offre_emploi}"



from django.db import models

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    response = models.TextField(null=True, blank=True)  # Champ pour la réponse de l'admin
    responded_at = models.DateTimeField(null=True, blank=True)  # Date de réponse
    is_answered = models.BooleanField(default=False)  # Indicateur de réponse

    def __str__(self):
        return f"Message de {self.name}"

