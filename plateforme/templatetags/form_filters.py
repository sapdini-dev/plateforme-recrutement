# myapp/templatetags/form_filters.py

from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    """
    Filtre pour ajouter une classe CSS à un widget de formulaire.
    """
    return value.as_widget(attrs={'class': arg})
