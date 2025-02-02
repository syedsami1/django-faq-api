# faq/apps.py
from django.apps import AppConfig

class FaqConfig(AppConfig):
    name = 'faq'

    def ready(self):
        import faq.signals  # noqa
