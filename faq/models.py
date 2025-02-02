# faq/models.py
from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

LANGUAGE_CHOICES = (
    ('en', 'English'),
    ('hi', 'Hindi'),
    ('bn', 'Bengali'),
)

class FAQ(models.Model):
    question = models.TextField(help_text="English question")
    answer = RichTextField(help_text="Answer in English (with rich text)")
    question_hi = models.TextField(blank=True, null=True, help_text="Hindi translation")
    question_bn = models.TextField(blank=True, null=True, help_text="Bengali translation")
    # You can add more fields if needed

    def get_translated_question(self, lang='en'):
        """
        Return translated question based on language code.
        Uses cache to store the result.
        """
        if lang == 'en':
            return self.question

        cache_key = f"faq_{self.pk}_question_{lang}"
        translated_text = cache.get(cache_key)
        if translated_text:
            return translated_text

        # Check if field is already set
        field_name = f"question_{lang}"
        translated_text = getattr(self, field_name, None)
        if translated_text:
            cache.set(cache_key, translated_text, timeout=3600)
            return translated_text

        # Fallback: translate dynamically using googletrans
        translation = translator.translate(self.question, dest=lang)
        translated_text = translation.text
        # Optionally, store translation in the model field and save (if desired)
        setattr(self, field_name, translated_text)
        self.save(update_fields=[field_name])
        cache.set(cache_key, translated_text, timeout=3600)
        return translated_text

    def __str__(self):
        return self.question
