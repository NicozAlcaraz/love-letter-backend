from rest_framework import viewsets
from shared.generic_viewset import GenericViewset
from .models import Reply
from .serializers import ReplySerializer


class ReplyViewset(GenericViewset, viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    protected_views = ["create", "update", "partial_update", "retrieve", "destroy"]