from django.apps import AppConfig

class PlateformeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plateforme'

    def ready(self):
        import plateforme.signals
