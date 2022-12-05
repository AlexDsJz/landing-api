from app.models import Contact, User
from django.shortcuts import get_object_or_404

def create_process(string_name, string_lastname, string_business, string_position, string_comment, string_email, user_id):
    
    user = get_object_or_404(User, pk = user_id)
    name = string_name 
    last = string_lastname
    business = string_business
    position = string_position
    comment = string_comment
    email = string_email
    
    contact = Contact.objects.create(name=name, business=business, position=position, user=user, lastname = last, comment = comment, email = email)
    contact.save()