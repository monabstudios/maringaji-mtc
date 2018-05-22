from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import permissions
from . import serializers
from . import models

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
  """Handles creating, reading and updating User Profiles."""

  print("hello")

  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)


class LoginViewSet(viewsets.ViewSet):
  """Handles logging in."""

  serializer_class = AuthTokenSerializer

  def create(self, request):
    return ObtainAuthToken().post(request)