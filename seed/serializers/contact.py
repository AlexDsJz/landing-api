"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Contact
from app.models import User

class ContactSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Contact
        fields = (
            'id',
            'created_at',
            'hash',
            'business',
            'comment',
            'lastname',
            'name',
            'position',
            'email',
            'user_id',  
        )