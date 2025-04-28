from django import views
from django.contrib import admin
from django.urls import path,include
from . views import*
from django.contrib import admin
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
from .views import  AvisCommuniquerView, PostulerAnnonceView, AnnonceRecrutementView
from django.urls import path
from .views import tableau_de_bord
from .views import (
    CandidatListView,
    CandidatDetailView,
    CandidatDeleteView,
)

from .views import ProfilUpdateView

from .views import (
    AccueilView,
    InformationView,
    VerifierCandidatView,
    ContacterNousView,
    
)
from django.urls import path
from .views import (
    AccueilView,
    InformationView,
    VerifierCandidatView,  # Remplacé de VerifierCandidatureView
    ContacterNousView,
      # Assurez-vous que ce nom est mis à jour aussi
    CandidatListView,      # Ajoutez ce chemin si nécessaire
    CandidatDetailView,    # Ajoutez ce chemin si nécessaire
    CandidatDeleteView,    # Ajoutez ce chemin si nécessaire
    CandidatUpdateView,    # Assurez-vous que ce nom est mis à jour aussi
)



from .views import RegionListView, RegionCreateView, LangueListView, LangueCreateView
from .views import LangueListView, LangueCreateView, LangueUpdateView, LangueDeleteView
from .views import DiplomeListView, DiplomeCreateView, DiplomeUpdateView, DiplomeDeleteView
from .views import AnnonceListView, AnnonceCreateView, AnnonceDetailView, AnnonceUpdateView, AnnonceDeleteView
from .views import AvisRecrutementListView, AvisRecrutementCreateView, AvisRecrutementUpdateView, AvisRecrutementDeleteView
from django.urls import path
from .views import UserCreateView

from .views import DetailEmploiView
from .views import (
    CandidatureOffreListView,
    CandidatureOffreDetailView,
    CandidatureOffreCreateView,
    CandidatureOffreUpdateView,
    CandidatureOffreDeleteView,)

from django.contrib.auth import views as auth_views

from .views import CandidatureListView

from .views import etat_candidature, accueil_candidat
from .views import some_error_page
from .views import candidature_success
from .views import contact_view
from django.urls import path
from .views import CandidatUpdateView, CandidatSuccessView
from .views import liste_messages, repondre_message
from .views import contact_view, response_message
from .views import historique_candidatures, ajouter_candidature
from .views import ressources
from .views import UserListView 
from .views import delete_user
from .views import admin_dashboard
from .views import ProfilView
from .views import CandidatEditView
from .views import CandidatDetailView
from .views import postuler
 

urlpatterns = [

    #postuller
    path('offre/<int:offre_id>/candidats/', candidats_par_offre, name='candidats_par_offre'),
    # autres URLs...
   path('candidatures/', CandidatureListView.as_view(), name='liste_candidatures'),


    path('crypto/', encrypt_decrypt_view, name='crypto_form'),
    path('candidat/ajouter/', CandidatCreateView.as_view(), name='candidat_create'),
    path('candidature/success/<int:id>/', candidature_success, name='candidature_success'),
    # ... autres URL
    path('offre/<int:offre_id>/postuler/', postuler, name='postuler'),
    path('candidature/success/', TemplateView.as_view(template_name='candidature_success.html'), name='candidature_success'),
    # Autres patterns...
    # Affichage du profil d'un candidat par ID
    path('profil/<int:pk>/', CandidatDetailView.as_view(), name='profil'),

    # Édition du profil d'un candidat par ID
    path('profil/edit/<int:pk>/', CandidatEditView.as_view(), name='profil_edit'),

    # Page de profil (générale, si nécessaire)
    path('profil/', ProfilView.as_view(), name='profil_view'),
    path('offre/<int:pk>/postuler/', PostulerView.as_view(), name='postuler'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
    path('users/', UserListView.as_view(), name='user_list'), 
    path('dashboard/',admin_dashboard, name='admin_dashboard'),
    #urls test en bas
    path('ressources/', ressources, name='ressources'),
    path('historique-candidatures/', historique_candidatures, name='historique_candidatures'),
    path('ajouter-candidature/<int:offre_id>/', ajouter_candidature, name='ajouter_candidature'),
    path('admin/messages/', liste_messages, name='liste_messages'),
    path('admin/messages/<int:message_id>/repondre/', repondre_message, name='repondre_message'),
    path('candidat/<int:pk>/update/', CandidatUpdateView.as_view(), name='candidat_update'),
    path('candidat/success/', CandidatSuccessView.as_view(), name='candidat_success'),  # Assurez-vous que ceci est défini
    path('candidature/traiter/', traiter_candidature, name='traiter_candidature'),
    path('candidature/success/<int:id>/', candidature_success, name='candidature_success'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', login_view, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('contact/', contact_view, name='contact'),
    path('messages/', contact_list, name='contact_list'),
    path('messages/', liste_messages, name='liste_messages'),

    path('mes-messages/', mes_messages, name='mes_messages'), 
    path('mes-messages/repondre/<int:message_id>/', response_message, name='response_message'),

    path('some-error-page/',some_error_page, name='some_error_page'),
    path('accueil-candidat/', accueil_candidat, name='accueil_candidat'),
    path('etat-candidature/', etat_candidature, name='etat_candidature'),
    path('verifier-candidature/', verifier_candidature, name='verifier_candidature'),
    path('mes-candidatures/', CandidatureListView.as_view(), name='candidature_list'),
    path('candidat/<int:pk>/', CandidatDetailView.as_view(), name='candidat_detail'),
    path('candidature-offre/', CandidatureOffreListView.as_view(), name='candidatureoffre_list'),
    path('candidature-offre/<int:pk>/', CandidatureOffreDetailView.as_view(), name='candidatureoffre_detail'),
    path('candidature-offre/ajouter/', CandidatureOffreCreateView.as_view(), name='candidatureoffre_create'),
    path('candidature-offre/<int:pk>/modifier/', CandidatureOffreUpdateView.as_view(), name='candidatureoffre_update'),
    path('candidature-offre/<int:pk>/supprimer/', CandidatureOffreDeleteView.as_view(), name='candidatureoffre_delete'),


    path('liste-des-candidats/', CandidatListView.as_view(), name='candidat_list'),
    path('ajouter-un-candidat/', CandidatCreateView.as_view(), name='candidat_create'),
    path('candidat/<int:pk>/', CandidatDetailView.as_view(), name='candidat_detail'),
    
    path('candidat/<int:pk>/update/', CandidatUpdateView.as_view(), name='candidat_update'),
    path('candidat/<int:pk>/supprimer/', CandidatDeleteView.as_view(), name='candidat_delete'),
    path('accueil/', AccueilView.as_view(), name='accueil'),
    path('information/', InformationView.as_view(), name='information'),
    path('verifier-candidat/', VerifierCandidatView.as_view(), name='verifier_candidat'),  # Remplacé de verifier_candidature
    path('contacter-nous/', ContacterNousView.as_view(), name='contacter_nous'),


#urls diplome
    path('liste des diplomes', DiplomeListView.as_view(), name='diplome_list'),
    path('ajouter un diplome', DiplomeCreateView.as_view(), name='diplome_create'),
    path('diplomes/<int:pk>/modifier/', DiplomeUpdateView.as_view(), name='diplome_update'),
    path('diplomes/<int:pk>/supprimer/', DiplomeDeleteView.as_view(), name='diplome_delete'),
#urls region et langue
    path('liste des regions', RegionListView.as_view(), name='region_list'),
    path('ajouter une region', RegionCreateView.as_view(), name='region_create'),
    path('regions/<int:pk>/modifier/', RegionUpdateView.as_view(), name='region_update'),
    path('regions/<int:pk>/supprimer/', RegionDeleteView.as_view(), name='region_delete'),
    path('liste des langues', LangueListView.as_view(), name='langue_list'),
    path('ajouter une langue', LangueCreateView.as_view(), name='langue_create'),
    path('langues/<int:pk>/modifier/', LangueUpdateView.as_view(), name='langue_update'),
    path('langues/<int:pk>/supprimer/', LangueDeleteView.as_view(), name='langue_delete'),
    #urls tableau de bord
    path('tableau_de_bord/',tableau_de_bord,name='tableau_de_bord'),
    path('accueil/', AccueilView.as_view(), name='Accueil'),
    path('information/', InformationView.as_view(), name='information'),
    path('contacter-nous/', ContacterNousView.as_view(), name='contacter_nous'),
    #annonce et recrutement
    path('basee',basee, name='basee' ),
    path('accueil',accueil,name='accueil'),
    path('tableau-de-bord/', tableau_de_bord, name='tableau_de_bord'),
    
    
    path('postuler-annonce/', PostulerAnnonceView.as_view(), name='postuler_annonce'),
    path('annonce-recrutement/', AnnonceRecrutementView.as_view(), name='annonce_recrutement'),
    #fin annonce et recrutement


    path('home', home, name='home' ),
    path('base',base,name='base'),
    path('basee',basee,name='basee'),
    
    path('success/', TemplateView.as_view(template_name='candidatures/candidature_success.html'), name='candidature_success'),

    
    path('liste des offres', listoffre, name='listoffre'),
    path('ajouter une offre', ajoutoffre, name='ajoutoffre'),
    path('offre/modifier/<int:pk>/', modifier_offre, name='modifier_offre'),  # Nouveau chemin pour modifier
    path('offre/supprimer/<int:pk>/', supprimer_offre, name='supprimer_offre'),
    path('offre/<int:pk>/', OffreDetailView.as_view(), name='detailoffre'),    
    path('recherche_emploi', recherche_emploi, name='recherche_emploi'),
    path('detail_emploi', detail_emploi, name='detail_emploi'),

    path('emploi/<int:pk>/', DetailEmploiView.as_view(), name='detail_emploi'),
    
    path('candidature/success/<int:id>/', TemplateView.as_view(template_name='candidature_success.html'), name='candidature_success'),
    path('candidature/success/', TemplateView.as_view(template_name='candidature_success.html'), name='candidature_success'),
    path('deconnexion', deconnexion, name='deconnexion'),
    #url annonce
    path('liste des annonces', AnnonceListView.as_view(), name='annonce_list'),
    path('ajouter une annonce', AnnonceCreateView.as_view(), name='annonce_create'),
    path('annonces/<int:pk>/', AnnonceDetailView.as_view(), name='annonce_detail'),
    path('annonces/<int:pk>/supprimer/', AnnonceDeleteView.as_view(), name='annonce_delete'),
    path('annonce/<int:pk>/update/', AnnonceUpdateView.as_view(), name='annonce_update'),
    path('liste-des-avis-de-recrutements/', AvisRecrutementListView.as_view(), name='avis_recrutement_list'),
    path('ajouter-un-avis-de-recrutement/', AvisRecrutementCreateView.as_view(), name='avis_recrutement_create'),
    path('avisrecrutement/<int:pk>/modifier/', AvisRecrutementUpdateView.as_view(), name='avis_recrutement_update'),
    path('avisrecrutement/<int:pk>/supprimer/', AvisRecrutementDeleteView.as_view(), name='avis_recrutement_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)