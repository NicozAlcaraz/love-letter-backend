from rest_framework import viewsets
from shared.generic_viewset import GenericViewset
from .models import Letters
from .serializers import LettersSerializer


class LettersViewset(GenericViewset, viewsets.ModelViewSet):
    queryset = Letters.objects.all()
    serializer_class = LettersSerializer

    protected_views = ["create", "update", "partial_update", "retrieve", "destroy"]