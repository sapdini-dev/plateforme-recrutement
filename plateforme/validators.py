from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class UniquePasswordValidator:
    def validate(self, password, user=None):
        if User.objects.filter(password=password).exists():
            raise ValidationError(
                _("Ce mot de passe est déjà utilisé par un autre utilisateur."),
                code='password_not_unique',
            )

    def get_help_text(self):
        return _("Votre mot de passe ne doit pas être similaire à celui d'un autre utilisateur.")
