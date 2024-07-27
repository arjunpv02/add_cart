from django.apps import AppConfig


class DeliveryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'delivery'
    
    def ready(self):
        import delivery.signals  # Ensure the signal is loaded when the app is ready
