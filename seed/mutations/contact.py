"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Contact
from app.models import User
from seed.schema.types import Contact as ContactType

class SaveContactMutation(graphene.Mutation):
    
    contact = graphene.Field(ContactType)
    
    class Arguments:
        business = graphene.String(required=True)
        comment = graphene.String(required=True)
        lastname = graphene.String(required=True)
        name = graphene.String(required=True)
        position = graphene.String(required=True)
        email = graphene.String(required=True)
        user = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        contact = {}
        if "business" in kwargs:
            contact["business"] = kwargs["business"]
        if "comment" in kwargs:
            contact["comment"] = kwargs["comment"]
        if "lastname" in kwargs:
            contact["lastname"] = kwargs["lastname"]
        if "name" in kwargs:
            contact["name"] = kwargs["name"]
        if "position" in kwargs:
            contact["position"] = kwargs["position"]
        if "email" in kwargs:
            contact["email"] = kwargs["email"]
        if "user" in kwargs:
            user = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["user"])
            contact["user"] = user
        contact = \
            Contact.objects.create(**contact)
        contact.save()
    
        return SaveContactMutation(
            contact=contact)

class SetContactMutation(graphene.Mutation):
    
    contact = graphene.Field(ContactType)
    
    class Arguments:
        id = graphene.Int(required=True)
        business = graphene.String(required=False)
        comment = graphene.String(required=False)
        lastname = graphene.String(required=False)
        name = graphene.String(required=False)
        position = graphene.String(required=False)
        email = graphene.String(required=False)
        user = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        contact = Contact.filter_permissions(
            Contact.objects,
            Contact.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "business" in kwargs:
            contact.business = kwargs["business"]
        if "comment" in kwargs:
            contact.comment = kwargs["comment"]
        if "lastname" in kwargs:
            contact.lastname = kwargs["lastname"]
        if "name" in kwargs:
            contact.name = kwargs["name"]
        if "position" in kwargs:
            contact.position = kwargs["position"]
        if "email" in kwargs:
            contact.email = kwargs["email"]
        if "user" in kwargs:
            user = User.objects \
                .get(pk=kwargs["user"])
            contact.user = user
        contact.save()
    
        return SetContactMutation(
            contact=contact)

class DeleteContactMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        contact_id = kwargs["id"]
        contact = Contact.objects.get(pk=kwargs["id"])
        contact.delete()
        return DeleteContactMutation(
            id=contact_id)