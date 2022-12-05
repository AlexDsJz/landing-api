"""
__Seed builder__
  AUTO_GENERATED Proxy (Read only)
  Modify via builder
"""

def get_contact_serializer():
    import seed.serializers.contact as SeedSerializer
    return SeedSerializer.ContactSerializer

def get_user_serializer():
    import seed.serializers.user as SeedSerializer
    return SeedSerializer.UserSerializer

def get_file_serializer():
    import seed.serializers.file as SeedSerializer
    return SeedSerializer.FileSerializer

ContactSerializer = get_contact_serializer()
UserSerializer = get_user_serializer()
FileSerializer = get_file_serializer()