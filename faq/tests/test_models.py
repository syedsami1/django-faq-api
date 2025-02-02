# faq/tests/test_models.py
import pytest
from faq.models import FAQ

@pytest.mark.django_db
def test_get_translated_question():
    faq = FAQ.objects.create(
        question="How are you?",
        answer="<p>I'm fine, thank you!</p>"
    )
    # English returns the original
    assert faq.get_translated_question('en') == "How are you?"
    # For another language, the method should return a non-empty string
    translated_hi = faq.get_translated_question('hi')
    assert translated_hi != ""
