# forms.py
from django import forms
from django import forms
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django import forms

from django import forms

from .models import OffreEmploi
from django import forms

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


from .models import Region, Langue

from django import forms
from .models import Region, Langue

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['nom']

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if Region.objects.filter(nom__iexact=nom).exists():
            raise forms.ValidationError("Cette région existe déjà.")
        return nom

class LangueForm(forms.ModelForm):
    class Meta:
        model = Langue
        fields = ['nom']

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if Langue.objects.filter(nom__iexact=nom).exists():
            raise forms.ValidationError("Cette langue existe déjà.")
        return nom

from .models import Diplome

class DiplomeForm(forms.ModelForm):
    class Meta:
        model = Diplome
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if Diplome.objects.filter(nom=nom).exists():
            raise forms.ValidationError('Ce diplôme existe déjà.')
        return nom


class ConnexionForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

from django import forms
from .models import OffreEmploi

# forms.py
from django import forms
from .models import AvisRecrutement

class AvisRecrutementForm(forms.ModelForm):
    class Meta:
        model = AvisRecrutement
        fields = ['numero', 'intitule', 'date_exp', 'document']  # Ajoutez les champs que vous souhaitez afficher





# forms.py
from django import forms
from .models import AvisRecrutement

class AvisRecrutementForm(forms.ModelForm):
    class Meta:
        model = AvisRecrutement
        fields = ['numero', 'intitule', 'date_exp', 'document']  # Inclure les champs nécessaires
        widgets = {
            'date_exp': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


#forms pour candidatures

# forms.py
from django import forms






from django import forms
from .models import OffreEmploi

class OffreEmploiForm(forms.ModelForm):
    class Meta:
        model = OffreEmploi
        fields = ['titre', 'description', 'date_exp', 'document']
        widgets = {
            'date_exp': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


from django import forms

# forms.py








        #forms pour l'annonce
    
from django import forms
from .models import Annonce

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titre', 'contenu','document']
        widgets = {
            'contenu': forms.Textarea(attrs={'class': 'form-control'}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),

        }


        #fins de orm pour l'annonce
        
# forms.p

#aujhourd'ui1
from .models import Candidat, Diplome, Langue, Region

from django import forms
from .models import Candidat

class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = [
            'nom', 'prenom', 'sexe', 'date_naissance', 'lieu_naissance', 'situation_matrimoniale',
            'telephone_contact', 'telephone_whatsapp', 'numero_identification', 'email',
            'dernier_diplome', 'region', 'situation_activite', 
            'langue_parlee1', 'langue_parlee2', 'langue_parlee3',
            'informatique', 'tablettes', 'enquete',
            'cv', 'certificat_nationalite', 'lettre_motivation',
            'copie_legalise_bac', 'copie_extrait_naissance',
            'certificat_domicile_ou_residence', 'atestation_enquete',
            

        ]
    
        
        widgets = {
            
            'sexe': forms.RadioSelect(choices=[('M', 'Homme'), ('F', 'Femme')]),
            'situation_matrimoniale': forms.Select(choices=Candidat.SITUATION_MATRIMONIALE_CHOICES),
            'langue_parlee1': forms.Select(),
            'langue_parlee2': forms.Select(),
            'langue_parlee3': forms.Select(),
            'region': forms.Select(),
            'informatique': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tablettes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enquete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
        }

from django import forms
from .models import Candidature, Candidat

class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ['candidat', 'offre_emploi']  # Supposant que vous avez ces champs dans votre modèle Candidature.

    def __init__(self, *args, **kwargs):
        super(CandidatureForm, self).__init__(*args, **kwargs)
        self.fields['candidat'].queryset = Candidat.objects.all()  # Assurant que le candidat est sélectionnable.




from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
#pour se connecter

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']


#forme pour la candidatureoffre

from django import forms
from .models import CandidatureOffre

class CandidatureOffreForm(forms.ModelForm):
    class Meta:
        model = CandidatureOffre
        fields = ['candidat', 'offre_emploi', 'statut']
        widgets = {
            'statut': forms.Select(choices=CandidatureOffre.STATUT_CHOICES),
        }
#verifier candidature

from django import forms

from django import forms

class CandidatVerificationForm(forms.Form):
    numero_identification = forms.CharField(
        label='Numéro d\'Identification',
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre numéro d\'identification'
        })
    )
    
    telephone_contact = forms.CharField(
        label='Téléphone de Contact',
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre numéro de téléphone de contact'
        })
    )




from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']


from django import forms
from .models import ContactMessage

class ResponseForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['response']
        widgets = {
            'response': forms.Textarea(attrs={'rows': 5}),
        }



class CryptoForm(forms.Form):
    text = forms.CharField(
        label="Saisissez votre texte",
        widget=forms.Textarea(attrs={
            'class': 'form-control form-control-lg shadow-sm',
            'placeholder': 'Entrez un texte...',
            'rows': 3
        }),
        required=True
    )
    action = forms.ChoiceField(
        choices=[('encrypt', '🔒 Chiffrer'), ('decrypt', '🔓 Déchiffrer')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True
    )
