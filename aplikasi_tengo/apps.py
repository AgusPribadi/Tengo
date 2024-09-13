from django.apps import AppConfig

class AplikasiTengoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "aplikasi_tengo"

def ready(self):
    import aplikasi_tengo.signals