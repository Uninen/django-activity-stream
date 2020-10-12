from django.apps import AppConfig


class CustomModelsConfig(AppConfig):
    name = 'custom_models'

    def ready(self):
        pass
