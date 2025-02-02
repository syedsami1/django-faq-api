# faq/tests/test_api.py
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_api_default_lang():
    FAQ.objects.create(
        question="What is Django?",
        answer="<p>Django is a high-level Python Web framework.</p>"
    )
    client = APIClient()
    url = reverse('faq-list')
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data[0]['translated_question'] == "What is Django?"

@pytest.mark.django_db
def test_faq_api_hindi():
    FAQ.objects.create(
        question="What is Django?",
        answer="<p>Django is a high-level Python Web framework.</p>"
    )
    client = APIClient()
    url = reverse('faq-list') + "?lang=hi"
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    # The Hindi translation should be non-empty and different from English
    assert data[0]['translated_question'] != "What is Django?"
