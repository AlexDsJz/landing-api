"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Contact
from app.serializers import ContactSerializer

class ContactViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Contact.filter_permissions(
            super().get_queryset(), Contact.permission_filters(user))