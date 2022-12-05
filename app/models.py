"""
__Seed builder__
  AUTO_GENERATED Proxy (Read only)
  Modify via builder
"""

def get_contact():
    import seed.models.contact as SeedModel
    return SeedModel.Contact

def get_user():
    import seed.models.user as SeedModel
    return SeedModel.User

def get_file():
    import seed.models.file as SeedFile
    return SeedFile.File

Contact = get_contact()
User = get_user()
File = get_file()