"""
__Seed builder__
  Extended module
"""

import seed.routes.contacts as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from seed.util.request_util import has_fields_or_400
from domain.contact import create_process

class ContactViewSet(SeedRoute.ContactViewSet):
    @action(detail = False, methods = ["POST"])
    def request_demo(self, request):
      
      data = request.data
      has_fields_or_400(data, "user_id", "business", "comment", "lastname", "name", "position", "email")
      
      user_id = int(data["user_id"])
      str_name = str(data["name"])
      str_last = str(data["lastname"])
      str_business = str(data["business"])
      str_position = str(data["position"])
      str_comment= str(data["comment"])
      str_email = str(data["email"])
      
      info = create_process(str_name, str_last, str_business, str_position, str_comment, str_email, user_id)
      
      return Response(status = status.HTTP_201_CREATED, data = info)
