from django.contrib import admin
from .models import Region, Langue, Diplome, Candidat, OffreEmploi, Annonce, AvisRecrutement, CandidatureOffre, ContactMessage


# Classe admin pour ContactMessage
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_answered')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('is_answered',)


# Classe admin pour Candidat
@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    # Afficher les champs supplémentaires dans la liste d'affichage
    list_display = ('nom', 'prenom', 'sexe', 'date_naissance', 'region', 'telephone_contact', 'email', 'dernier_diplome')
    
    # Ajouter d'autres champs dans la barre de recherche
    search_fields = ('nom', 'prenom', 'numero_identification', 'telephone_contact', 'email')
    
    # Ajouter des filtres pour ces champs
    list_filter = ('sexe', 'region', 'dernier_diplome', 'situation_matrimoniale', 'informatique', 'tablettes', 'enquete')


# Enregistrer les autres modèles dans l'admin sans classe admin personnalisée
admin.site.register(Region)
admin.site.register(Langue)
admin.site.register(Diplome)
admin.site.register(OffreEmploi)
admin.site.register(Annonce)
admin.site.register(AvisRecrutement)
admin.site.register(CandidatureOffre)
admin.site.register(ContactMessage, ContactMessageAdmin)
