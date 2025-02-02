# faq/views.py
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

class FAQListAPIView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()

    # Optionally, override get_queryset to prefetch or optimize further.
