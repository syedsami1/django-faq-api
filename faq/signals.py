# faq/signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import FAQ
from googletrans import Translator

translator = Translator()

@receiver(pre_save, sender=FAQ)
def auto_translate_faq(sender, instance, **kwargs):
    # Auto-translate if translations are empty
    if not instance.question_hi:
        instance.question_hi = translator.translate(instance.question, dest='hi').text
    if not instance.question_bn:
        instance.question_bn = translator.translate(instance.question, dest='bn').text
