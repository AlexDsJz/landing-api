"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'created_at',
            'hash',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',  
        )