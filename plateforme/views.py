from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from datetime import date
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import get_object_or_404
from django.views.generic import DeleteView

from django.shortcuts import render
from .models import OffreEmploi, Annonce  # Import both models
from django.utils import timezone

def home(request):
    today = timezone.now().date()
    offres = OffreEmploi.objects.all()  # Retrieve all job offers
    annonces = Annonce.objects.all()  # Retrieve all announcements

    # Pass both 'offres' and 'annonces' to the template context
    return render(request, 'home.html', {'offres': offres, 'annonces': annonces, 'today': today})














def accueil(request):
    return render(request,'accueil.html')

def base(request):
    return render(request, 'base.html')
def basee(request):
    return render(request,'basee.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import OffreEmploi
from .forms import OffreEmploiForm



from django.utils import timezone
from django.shortcuts import render
from .models import OffreEmploi

def listoffre(request):
    today = timezone.now().date()  # Obtenir la date actuelle
    offres = OffreEmploi.objects.all()
    return render(request, 'listoffre.html', {'offres': offres, 'today': today})

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def ajoutoffre(request):
    if request.method == 'POST':
        form = OffreEmploiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listoffre')
    else:
        form = OffreEmploiForm()
    return render(request, 'ajoutoffre.html', {'form': form})

class AjouterOffreView(CreateView):
    model = OffreEmploi
    form_class = OffreEmploiForm
    template_name = 'ajoutoffre.html'
    success_url = reverse_lazy('liste des offres')

def detail_emploi(request, id):
    offre = get_object_or_404(OffreEmploi, id=id)
    return render(request, 'detail_emploi.html', {'offre': offre})

class OffreDetailView(DetailView):
    model = OffreEmploi
    template_name = 'offre_detail.html'
    context_object_name = 'offre'

def recherche_emploi(request):
    query = request.GET.get('q', '')
    location = request.GET.get('location', '')
    offres = OffreEmploi.objects.all()

    if query:
        offres = offres.filter(Q(titre__icontains=query) | Q(description__icontains=query))
    if location:
        offres = offres.filter(location__icontains=location)

    return render(request, 'recherche_emploi.html', {'offres': offres})




from django.shortcuts import render, get_object_or_404, redirect
from .models import OffreEmploi
from .forms import OffreEmploiForm

# Vue pour modifier une offre
def modifier_offre(request, pk):
    offre = get_object_or_404(OffreEmploi, pk=pk)
    if request.method == 'POST':
        form = OffreEmploiForm(request.POST, instance=offre)
        if form.is_valid():
            form.save()
            return redirect('listoffre')  # Redirige vers la liste des offres après la modification
    else:
        form = OffreEmploiForm(instance=offre)
    return render(request, 'modifier_offre.html', {'form': form, 'offre': offre})

# Vue pour supprimer une offre
def supprimer_offre(request, pk):
    offre = get_object_or_404(OffreEmploi, pk=pk)
    if request.method == 'POST':
        offre.delete()
        return redirect('listoffre')  # Redirige vers la liste des offres après la suppression
    return render(request, 'supprimer_offre.html', {'offre': offre})









def deconnexion(request):
    logout(request)
    return redirect('home')

def avis_recrutement_list(request):
    avis_list = AvisRecrutement.objects.all()
    return render(request, 'avis_recrutement_list.html', {'avis_list': avis_list})


from django.views.generic import TemplateView


# Vue pour l'avis de communiquer
class AvisCommuniquerView(TemplateView):
    template_name = 'avis_communiquer.html'
    

# Vue pour postuler sur l'annonce
class PostulerAnnonceView(TemplateView):
    template_name = 'postuler_annonce.html'

# Vue pour la page principale (annonce et recrutement)
class AnnonceRecrutementView(TemplateView):
    template_name = 'annonce_recrutement.html'

#views pour le tableau de bord


from django.shortcuts import render
from django.utils import timezone
from .models import OffreEmploi

def tableau_de_bord(request):
    today = timezone.now().date()

    offres = OffreEmploi.objects.all()
    return render(request, 'tableau_de_bord.html', {'offres': offres, 'today': today})






#views postulerfrom django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Candidat, OffreEmploi
from .forms import CandidatForm

class PostulerView(CreateView):
    model = Candidat
    form_class = CandidatForm
    template_name = 'candidat_form.html'

    def form_valid(self, form):
        # On récupère l'offre à partir de l'URL et on l'associe à la candidature
        form.instance.offre = OffreEmploi.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('candidature_success')

#views puour les lien dans tableau de bord
# views.py

from django.views.generic import ListView, CreateView
from .models import Region, Langue
from .forms import RegionForm, LangueForm

class RegionListView(ListView):
    model = Region
    template_name = 'region_list.html'
    context_object_name = 'regions'

class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm
    template_name = 'region_form.html'
    success_url = 'liste des regions'

class LangueListView(ListView):
    model = Langue
    template_name = 'langue_list.html'
    context_object_name = 'langues'

class LangueCreateView(CreateView):
    model = Langue
    form_class = LangueForm
    template_name = 'langue_form.html'
    success_url = 'liste des langues'

#views pour modifier et supprimer
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import Region, Langue
from .forms import RegionForm, LangueForm

class RegionUpdateView(UpdateView):
    model = Region
    form_class = RegionForm
    template_name = 'region_form.html'
    success_url = reverse_lazy('region_list')

class RegionDeleteView(DeleteView):
    model = Region
    template_name = 'region_confirm_delete.html'
    success_url = reverse_lazy('region_list')

class LangueUpdateView(UpdateView):
    model = Langue
    form_class = LangueForm
    template_name = 'langue_form.html'
    success_url = reverse_lazy('langue_list')

class LangueDeleteView(DeleteView):
    model = Langue
    template_name = 'langue_confirm_delete.html'
    success_url = reverse_lazy('langue_list')


#views pour diplome
# views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Diplome
from .forms import DiplomeForm

class DiplomeListView(ListView):
    model = Diplome
    template_name = 'diplome_list.html'
    context_object_name = 'diplomes'

class DiplomeCreateView(CreateView):
    model = Diplome
    form_class = DiplomeForm
    template_name = 'diplome_form.html'
    success_url = ('liste des diplomes')

class DiplomeUpdateView(UpdateView):
    model = Diplome
    form_class = DiplomeForm
    template_name = 'diplome_form.html'
    success_url = reverse_lazy('diplome_list')

class DiplomeDeleteView(DeleteView):
    model = Diplome
    template_name = 'diplome_confirm_delete.html'
    success_url = reverse_lazy('diplome_list')
#views pour les candidature
# views.py


    #views pour les annonce
    
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from .models import Annonce
from .forms import AnnonceForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView

class AnnonceDeleteView(DeleteView):
    model = Annonce
    template_name = 'annonce_confirm_delete.html'
    success_url = reverse_lazy('annonce_list')

class AnnonceListView(ListView):
    model = Annonce
    template_name = 'annonce_list.html'
    context_object_name = 'annonces'
    ordering = ['-date_pub']  # Pour afficher les annonces les plus récentes en premier

class AnnonceCreateView(CreateView):
    model = Annonce
    form_class = AnnonceForm
    template_name = 'annonce_form.html'
    success_url = ('liste des annonces') # Redirection après la création

class AnnonceDetailView(DetailView):
    model = Annonce
    template_name = 'annonce_detail.html'
    context_object_name = 'annonce'


class AnnonceUpdateView(UpdateView):
    model = Annonce
    fields = ['titre', 'contenu']
    template_name = 'annonce_form.html'
    success_url = reverse_lazy('annonce_list')
#fin de views de l'annonce

from django.views.generic.edit import CreateView
from .models import AvisRecrutement
from .forms import AvisRecrutementForm
from django.urls import reverse_lazy


from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import AvisRecrutement
from .forms import AvisRecrutementForm

class AvisRecrutementCreateView(CreateView):
    model = AvisRecrutement
    form_class = AvisRecrutementForm  # Formulaire à utiliser
    template_name = 'avis_recrutement_form.html'  # Template à utiliser pour afficher le formulaire
    success_url = reverse_lazy('avis_recrutement_list')  # Redirection après la création



from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import AvisRecrutement
from .forms import AvisRecrutementForm

class AvisRecrutementUpdateView(UpdateView):
    model = AvisRecrutement
    form_class = AvisRecrutementForm  # Formulaire à utiliser
    template_name = 'avis_recrutement_form.html'  # Template à utiliser
    success_url = reverse_lazy('avis_recrutement_list')  # Redirection après la mise à jour



from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import AvisRecrutement

class AvisRecrutementDeleteView(DeleteView):
    model = AvisRecrutement
    template_name = 'avis_recrutement_confirm_delete.html'  # Template de confirmation avant suppression
    success_url = reverse_lazy('avis_recrutement_list')  # Redirection après la suppression



from django.views.generic import ListView
from .models import AvisRecrutement

class AvisRecrutementListView(ListView):
    model = AvisRecrutement
    template_name = 'avis_recrutement_list.html'  # Nom du template
    context_object_name = 'avis_recrutements'  # Nom utilisé dans le template pour accéder aux avis
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    






from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Candidat
from .forms import CandidatForm



# views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotAllowed

def candidature_success(request, id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    candidat = get_object_or_404(Candidat, id=id)
    return render(request, 'candidature_success.html')






from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from .models import Candidat
from .forms import CandidatForm

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib import messages
from .models import Candidat, OffreEmploi
from .forms import CandidatForm

class CandidatCreateView(CreateView):
    model = Candidat
    form_class = CandidatForm
    num_steps = 4
    template_name = 'candidat_form.html'

    def form_valid(self, form):
        # Récupérer l'ID de l'offre d'emploi à partir de la requête
        offre_id = self.request.GET.get('offre_id')
        if offre_id:
            try:
                form.instance.offre_emploi = OffreEmploi.objects.get(id=offre_id)
            except OffreEmploi.DoesNotExist:
                messages.error(self.request, "L'offre d'emploi n'existe pas.")
                return redirect('some_error_page')  # Rediriger vers une page d'erreur appropriée

        # Enregistrer l'instance du candidat
        candidat = form.save()

        # Afficher un message de succès
        messages.success(self.request, "Votre candidature a été soumise avec succès.")
        
        # Rediriger vers la page de succès avec l'ID du candidat
        return redirect('candidature_success', id=candidat.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_steps'] = self.num_steps
        context['step_range'] = range(self.num_steps)
        return context

# views.py
from django.shortcuts import render
from django.views import View

class ProfilView(View):
    def get(self, request):
        # Gérer les requêtes GET
        return render(request, 'profil.html')

    def post(self, request):
        # Gérer les requêtes POST
        # Traitez le formulaire ou d'autres données envoyées via POST ici
        return render(request, 'profil.html')



from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Candidat

class CandidatProfileView(DetailView):
    model = Candidat
    template_name = 'profil.html'
    context_object_name = 'candidat'

    def get_object(self, queryset=None):
        # Assurez-vous que vous récupérez l'utilisateur connecté
        return get_object_or_404(Candidat, id=self.request.user.candidat.id)

from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .models import Candidat

class CandidatDetailView(DetailView):
    model = Candidat
    template_name = 'profil.html'
    context_object_name = 'candidat'

    def get_object(self, queryset=None):
        # Récupérer le candidat à partir de l'URL (pk)
        pk = self.kwargs.get('pk')
        return get_object_or_404(Candidat, pk=pk)
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from .models import Candidat
from django.urls import reverse_lazy

class CandidatEditView(UpdateView):
    model = Candidat
    template_name = 'profil_edit.html'
    fields = '__all__'  # Ou spécifiez les champs que vous souhaitez afficher
    success_url = reverse_lazy('profil')  # Redirection après la mise à jour

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Candidat, pk=pk)


# views.py

from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Candidat
from .forms import CandidatForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import Candidat
from .forms import CandidatForm

class CandidatUpdateView(UpdateView):
    model = Candidat
    form_class = CandidatForm
    template_name = 'candidat_form.html'
    success_url = reverse_lazy('profil')




class CandidatDetailView(DetailView):
    model = Candidat
    template_name = 'candidat_detail.html'
    context_object_name = 'candidat'
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Candidat
from .forms import CandidatForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import Candidat
from .forms import CandidatForm

class CandidatUpdateView(UpdateView):
    model = Candidat
    form_class = CandidatForm
    template_name = 'candidat_update.html'
    success_url = reverse_lazy('candidat_success')

    def get_context_data(self, **kwargs):
        # Appel du contexte de base
        context = super().get_context_data(**kwargs)
        # Ajouter le numéro de vérification au contexte
        context['id_verification'] = self.object.numero_identification
        return context

    def form_valid(self, form):
        # Optionnel : Ajoutez un traitement personnalisé si nécessaire avant de sauvegarder
        return super().form_valid(form)

    def form_invalid(self, form):
        # Optionnel : Gérez les cas où les données du formulaire sont invalides
        return super().form_invalid(form)


from django.views.generic import TemplateView

class CandidatSuccessView(TemplateView):
    template_name = 'candidat_success.html'




class CandidatDeleteView(DeleteView):
    model = Candidat
    template_name = 'candidat_confirm_delete.html'
    success_url = reverse_lazy('candidat_list')

class CandidatListView(ListView):
    model = Candidat
    template_name = 'candidat_list.html'
    context_object_name = 'candidats'



from django.views.generic import TemplateView
from .models import OffreEmploi, Candidat  # Assurez-vous que le modèle est correct

class AccueilView(TemplateView):
    template_name = 'accueil.html'

class InformationView(TemplateView):
    template_name = 'information.html'

class VerifierCandidatView(TemplateView):  # Mise à jour du nom de la vue
    template_name = 'verifier_candidat.html'

class ContacterNousView(TemplateView):
    template_name = 'contacter_nous.html'


#candidature avec des candidat




#views connection form
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tableau_de_bord')  # Redirection après connexion
            else:
                form.add_error(None, 'Identifiants invalides.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})




#views pour inscription
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Sauvegarder l'utilisateur et se connecter automatiquement
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

#views creer une candidature

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import CandidatureOffre
from .forms import CandidatureOffreForm

class CandidatureOffreCreateView(CreateView):
    model = CandidatureOffre
    form_class = CandidatureOffreForm
    template_name = 'candidatureoffre_form.html'
    success_url = reverse_lazy('candidatureoffre_list')

    def form_valid(self, form):
        try:
            # Vérifiez si l'utilisateur connecté a un objet `Candidat`
            candidat = self.request.user.candidat
        except ObjectDoesNotExist:
            # Redirigez vers une page pour créer un candidat si l'utilisateur n'a pas de candidat
            return redirect('candidat_create')  # Remplacez par l'URL appropriée

        # Si le candidat existe, associez-le à la candidature
        form.instance.candidat = candidat
        return super().form_valid(form)


#views pour lister tout les candidatures

# views.py
from django.views.generic import ListView
from .models import CandidatureOffre

class CandidatureOffreListView(ListView):
    model = CandidatureOffre
    template_name = 'candidatureoffre_list.html'
    context_object_name = 'candidatures_offre'
#views pour afficher les detaille de candidature 

from django.views.generic import DetailView
from .models import CandidatureOffre

class CandidatureOffreDetailView(DetailView):
    model = CandidatureOffre
    template_name = 'candidatureoffre_detail.html'
    context_object_name = 'candidature_offre'
#views pour modifier une candidature

from django.views.generic.edit import UpdateView
from .models import CandidatureOffre

class CandidatureOffreUpdateView(UpdateView):
    model = CandidatureOffre
    fields = ['statut']
    template_name = 'candidatureoffre_form.html'
    success_url = '/candidature-offre/'  # Redirige vers la liste des candidatures
#views pour supprimer une candidature

from django.views.generic.edit import DeleteView
from .models import CandidatureOffre

class CandidatureOffreDeleteView(DeleteView):
    model = CandidatureOffre
    template_name = 'candidatureoffre_confirm_delete.html'
    success_url = '/candidature-offre/'  # Redirige vers la liste des candidatures





from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import CandidatureOffreForm
from .models import Candidat


def candidature_offre_create(request):
    # Vérifiez que l'utilisateur est authentifié
    if not request.user.is_authenticated:
        return redirect('login')  # Remplacez par votre URL de connexion

    # Récupérer le candidat associé à l'utilisateur
    try:
        candidat = Candidat.objects.get(user=request.user)
    except Candidat.DoesNotExist:
        # Gérer le cas où le profil Candidat n'existe pas
        return redirect('error_page')  # Redirigez vers une page d'erreur ou créez un profil Candidat

    if request.method == 'POST':
        form = CandidatureOffreForm(request.POST)
        if form.is_valid():
            candidature = form.save(commit=False)
            candidature.candidat = candidat  # Associer le candidat à la candidature
            candidature.save()
            return redirect('candidatureoffre_list')
    else:
        form = CandidatureOffreForm()
    
    return render(request, 'candidature_offre_form.html', {'form': form})


#eieiiirr

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Candidat

class CandidatureListView(LoginRequiredMixin, ListView):
    model = Candidat
    template_name = 'candidature_list.html'
    context_object_name = 'candidatures'

    def get_queryset(self):
        # Filtrer les candidatures pour l'utilisateur connecté
        return Candidat.objects.filter(user=self.request.user)
#verifier candidature
from django.shortcuts import render
from .forms import CandidatVerificationForm
from .models import Candidat
from django.shortcuts import render
from .models import Candidat, CandidatureOffre
from .forms import CandidatVerificationForm
from django.shortcuts import render
from .forms import CandidatVerificationForm
from .models import Candidat, CandidatureOffre

def verifier_candidature(request):
    if request.method == 'POST':
        form = CandidatVerificationForm(request.POST)
        if form.is_valid():
            telephone_contact = form.cleaned_data['telephone_contact']
            
            # Rechercher les candidats en fonction du téléphone de contact
            candidats = Candidat.objects.filter(telephone_contact=telephone_contact)

            if not candidats.exists():
                message = 'Aucun candidat trouvé avec ces informations.'
                return render(request, 'verifier_candidature.html', {'form': form, 'message': message})

            # Si plusieurs candidats sont trouvés, gérer cela
            if candidats.count() > 1:
                message = 'Plusieurs candidats ont été trouvés avec ce numéro de téléphone. Veuillez contacter l\'administration.'
                return render(request, 'verifier_candidature.html', {'form': form, 'message': message})

            # Si un seul candidat est trouvé
            candidat = candidats.first()

            # Rechercher la candidature associée au candidat
            candidature = CandidatureOffre.objects.filter(candidat=candidat).first()
            if candidature:
                offre_emploi = candidature.offre_emploi
                date_candidature = candidature.date_candidature
                statut_candidature = candidature.statut

                # Déterminer le message à afficher en fonction du statut
                if statut_candidature == 'ACCEPTE':
                    message = "Félicitations ! Votre candidature a été acceptée."
                else:
                    message = "Malheureusement, vous n'avez pas encore été accepté. Veuillez consulter ultérieurement."

                context = {
                    'form': form,
                    'offre_emploi': offre_emploi,
                    'date_candidature': date_candidature,
                    'statut_candidature': statut_candidature,
                    'message': message,
                }
                return render(request, 'verifier_candidature.html', context)
            else:
                message = "Aucune candidature trouvée pour ce candidat."
                return render(request, 'verifier_candidature.html', {'form': form, 'message': message})
                
    else:
        form = CandidatVerificationForm()

    return render(request, 'verifier_candidature.html', {'form': form})


from django.shortcuts import render
from .models import Candidat

def candidature_list(request):
    user = request.user
    if user.is_authenticated:
        candidatures = Candidat.objects.filter(user=user)
    else:
        candidatures = Candidat.objects.none()  # Aucune candidature si l'utilisateur n'est pas connecté

    return render(request, 'candidature_list.html', {'candidatures': candidatures})

from django.views.generic.detail import DetailView
from .models import Candidat

class CandidatDetailView(DetailView):
    model = Candidat
    template_name = 'candidat_detail.html'
    context_object_name = 'candidat'
#etat de ma candidature 

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Candidat, CandidatureOffre


def etat_candidature(request):
    try:
        # Récupérer l'objet Candidat associé à l'utilisateur connecté
        candidat = Candidat.objects.get(user=request.user)
    except Candidat.DoesNotExist:
        return render(request, 'etat_candidature.html', {'message': 'Candidat non trouvé.'})

    # Récupérer toutes les candidatures associées au candidat
    candidatures = CandidatureOffre.objects.filter(candidat=candidat)

    return render(request, 'etat_candidature.html', {'candidatures': candidatures})




from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ContactMessage


def accueil_candidat(request):
    # Récupérer les messages et leurs réponses pour l'utilisateur connecté
    messages = ContactMessage.objects.filter(email=request.user.email)
    
    return render(request, 'accueil_candidat.html', {'messages': messages})





# views.py
from django.shortcuts import render, get_object_or_404
from .models import Candidat

def some_error_page(request):
    candidat = get_object_or_404(Candidat, user=request.user)
    return render(request, 'some_error_page.html', {'candidat': candidat})
#modifier profile 

# views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Candidat
from .forms import CandidatForm

class ProfilUpdateView(UpdateView):
    model = Candidat
    form_class = CandidatForm
    template_name = 'modifie_profil_candidat.html'
    success_url = reverse_lazy('candidature_success')  # Remplacez par l'URL où rediriger après la modification



# views.py
from django.views.generic import DetailView
from .models import OffreEmploi

class DetailEmploiView(DetailView):
    model = OffreEmploi
    template_name = 'detail_emploi.html'
    context_object_name = 'emploi'



def contact_view(request):
    return render(request, 'contact.html')



from django.shortcuts import render
from .models import ContactMessage

def contact_list(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'contact_list.html', {'messages': messages})

    


# views.py

from django.shortcuts import render

#traitement des candidatures 
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CandidatForm  # Assurez-vous d'importer votre formulaire
from .models import Candidat, CandidatureOffre

def traiter_candidature(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST)
        if form.is_valid():
            # Sauvegarder la candidature
            candidature = form.save(commit=False)
            # Assurez-vous que le candidat est associé à l'utilisateur courant
            candidature.candidat = get_object_or_404(Candidat, user=request.user)
            candidature.save()

            # Obtenir l'ID de la candidature pour redirection
            candidat_id = candidature.candidat.id  # ou tout autre champ que vous souhaitez utiliser
            return redirect('candidature_success', id=candidat_id)
    else:
        form = CandidatForm()

    return render(request, 'candidat_form.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import CandidatForm

#view complet 



from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import ContactMessage
from .forms import ContactForm, ResponseForm

# Vue pour envoyer un message de contact
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import ContactMessage
from .forms import ContactForm, ResponseForm

# Vue pour envoyer un message de contact
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre le message dans la base de données
            return redirect('home')  # Redirige vers une page de confirmation ou d'accueil
    else:
        form = ContactForm()  # Formulaire vide pour GET request

    return render(request, 'contact.html', {'form': form})

# Vérification si l'utilisateur est un admin
def admin_required(user):
    return user.is_staff

# Vue pour lister les messages (admin seulement)
@user_passes_test(admin_required)
def liste_messages(request):
    messages = ContactMessage.objects.all()
    return render(request, 'liste_messages.html', {'messages': messages})

# Vue pour répondre à un message (admin seulement)
@user_passes_test(admin_required)
def repondre_message(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)

    if request.method == 'POST':
        form = ResponseForm(request.POST, instance=message)
        if form.is_valid():
            message = form.save(commit=False)
            message.is_answered = True
            message.responded_at = timezone.now()
            message.save()
            return redirect('liste_messages')  # Redirection après la réponse
    else:
        form = ResponseForm(instance=message)

    return render(request, 'repondre_message.html', {'form': form, 'message': message})

# Vue pour afficher les messages d'un utilisateur connecté
@login_required
def mes_messages(request):
    # Récupérer les messages de l'utilisateur connecté
    messages = ContactMessage.objects.filter(email=request.user.email)
    return render(request, 'mes_messages.html', {'messages': messages})

# Vue pour afficher et répondre aux messages par l'administrateur
@user_passes_test(admin_required)
def response_message(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)

    if request.method == 'POST':
        form = ResponseForm(request.POST, instance=message)
        if form.is_valid():
            response_message = form.save(commit=False)
            response_message.is_answered = True
            response_message.responded_at = timezone.now()  # Date de réponse
            response_message.save()
            return redirect('liste_messages')  # Redirection après réponse
    else:
        form = ResponseForm(instance=message)

    return render(request, 'response_message.html', {'form': form, 'message': message})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ContactMessage

@login_required
def mes_messages(request):
    # Récupérer les messages de l'utilisateur connecté
    messages = ContactMessage.objects.filter(email=request.user.email)
    return render(request, 'mes_messages.html', {'messages': messages})


# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CandidatureOffre

@login_required
def historique_candidatures(request):
    candidatures = CandidatureOffre.objects.filter(candidat=request.user.candidat).order_by('-date_candidature')
    return render(request, 'historique_candidatures.html', {'candidatures': candidatures})


# views.py
from django.shortcuts import redirect, render
from .forms import CandidatureOffreForm

@login_required
def ajouter_candidature(request, offre_id):
    offre = get_object_or_404(OffreEmploi, id=offre_id)
    
    if request.method == 'POST':
        form = CandidatureOffreForm(request.POST)
        if form.is_valid():
            candidature = form.save(commit=False)
            candidature.candidat = request.user.candidat
            candidature.offre_emploi = offre
            candidature.save()
            return redirect('historique_candidatures')  # Redirige vers l'historique des candidatures
    else:
        form = CandidatureOffreForm()

    return render(request, 'ajouter_candidature.html', {'form': form, 'offre': offre})


# views.py
def ressources(request):
    return render(request, 'ressources.html')



# plateforme/views.py
# plateforme/views.py

from django.shortcuts import render
from .models import Candidat, OffreEmploi, CandidatureOffre, Annonce
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_dashboard(request):
    total_candidats = Candidat.objects.count()
    total_offres = OffreEmploi.objects.count()
    total_candidatures = CandidatureOffre.objects.count()
    total_annonces = Annonce.objects.count()

    context = {
        'total_candidats': total_candidats,
        'total_offres': total_offres,
        'total_candidatures': total_candidatures,
        'total_annonces': total_annonces,
    }
    return render(request, 'admin_dashboard.html', context)


# pour les utulisateur

# In your views.py file
from django.views.generic import ListView
from django.contrib.auth.models import User  # Assuming you're using Django's built-in User model

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'  # Create this template to display the list of users
    context_object_name = 'users'  # This will be available in the template as 'users'


#supprimer un utulisateur

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Candidat, CandidatureOffre
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Candidat, CandidatureOffre

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # Supprimer les candidatures associées
    CandidatureOffre.objects.filter(candidat__user=user).delete()

    # Supprimer le candidat associé
    Candidat.objects.filter(user=user).delete()

    # Puis supprimer l'utilisateur
    user.delete()
    
    return redirect('user_list')  # Rediriger vers la liste des utilisateurs


from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Candidat, OffreEmploi
from .forms import CandidatForm

class PostulerView(CreateView):
    model = Candidat
    form_class = CandidatForm
    template_name = 'candidature_form.html'

    def form_valid(self, form):
        # On récupère l'offre à partir de l'URL et on l'associe à la candidature
        form.instance.offre = OffreEmploi.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('candidature_success')


from django.shortcuts import render, get_object_or_404, redirect
from .models import OffreEmploi, Candidature
from .forms import CandidatureForm

def postuler(request, offre_id):
    offre = get_object_or_404(OffreEmploi, id=offre_id)
    if request.method == 'POST':
        candidat = request.user.candidat  # Supposons que l'utilisateur est lié à un candidat
        # Créez une candidature
        candidature = Candidature(candidat=candidat, offre_emploi=offre)
        candidature.save()
        return redirect('candidature_success')  # Rediriger vers une page de succès
    return render(request, 'postuler.html', {'offre': offre})


from django.shortcuts import render
from .models import Candidature

def liste_candidatures(request):
    candidatures = Candidature.objects.select_related('candidat', 'offre_emploi').all()
    return render(request, 'liste_candidatures.html', {'candidatures': candidatures})

# views.py
from django.shortcuts import redirect

def CandidatureCreateView(request):
    if request.method == 'POST':
        form = CandidatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidature_success')  # Redirection vers la page de succès
    else:
        form = CandidatureForm()
    return render(request, 'candidat_form.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import CandidatForm, CandidatureForm

def submit_application(request):
    if request.method == 'POST':
        candidat_form = CandidatForm(request.POST, request.FILES)
        candidature_form = CandidatureForm(request.POST)

        if candidat_form.is_valid() and candidature_form.is_valid():
            candidat = candidat_form.save()  # Enregistre le candidat
            candidature = candidature_form.save(commit=False)
            candidature.candidat = candidat  # Lien entre la candidature et le candidat nouvellement créé
            candidature.save()  # Enregistre la candidature
            return redirect('candidature_success')  # Redirige vers une page de succès

    else:
        candidat_form = CandidatForm()
        candidature_form = CandidatureForm()

    return render(request, 'candidat_form.html', {
        'candidat_form': candidat_form,
        'candidature_form': candidature_form,
    })

    from django.views.generic import ListView
from .models import Candidature

class CandidatureListView(ListView):
    model = Candidat
    template_name = 'liste_candidatures.html'
    context_object_name = 'candidatures'


# views.py
from django.shortcuts import render, get_object_or_404
from .models import OffreEmploi, Candidature

def candidats_par_offre(request, offre_id):
    offre = get_object_or_404(OffreEmploi, id=offre_id)
    candidat = Candidat.objects.filter(offre_emploi=offre)
    return render(request, 'candidats_par_offre.html', {'offre': offre, 'candidat': candidat})


# views.py
from django.shortcuts import render
from .models import OffreEmploi, Candidature

def lister_offres_et_candidats(request):
    offres = OffreEmploi.objects.all()  # Récupère toutes les offres d'emploi
    # Optionnel : récupérer les candidatures associées à chaque offre
    offres_avec_candidats = [
        {
            'offre': offre,
            'candidat': Candidat.objects.filter(offre_emploi=offre)
        }
        for offre in offres
    ]
    return render(request, 'lister_offres_et_candidats.html', {'offres_avec_candidats': offres_avec_candidats})


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from django.shortcuts import render
from .forms import CryptoForm
import base64


SECRET_KEY = b'MaCleSecrete1234'  # Clé secrète (16 octets)

def encrypt(text):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ciphertext).decode()

def decrypt(encrypted_text):
    try:
        encrypted_data = base64.b64decode(encrypted_text)
        iv = encrypted_data[:AES.block_size]
        ciphertext = encrypted_data[AES.block_size:]

        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
    except Exception:
        return "Erreur : Texte invalide ou clé incorrecte"

def encrypt_decrypt_view(request):
    result = None
    form = CryptoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        action = form.cleaned_data['action']
        result = encrypt(text) if action == 'encrypt' else decrypt(text)

    return render(request, 'crypto_form.html', {'form': form, 'result': result})