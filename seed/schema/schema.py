"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene

import seed.schema.types
import seed.mutations.contact
import seed.mutations.user

class Query(seed.schema.types.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    saveContact = seed.mutations.contact \
        .SaveContactMutation.Field()
    setContact = seed.mutations.contact \
        .SetContactMutation.Field()
    deleteContact = seed.mutations.contact \
        .DeleteContactMutation.Field()
    saveUser = seed.mutations.user \
        .SaveUserMutation.Field()
    setUser = seed.mutations.user \
        .SetUserMutation.Field()
    deleteUser = seed.mutations.user \
        .DeleteUserMutation.Field()
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)