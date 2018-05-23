from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

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


class ApplicationApiView(APIView):
  """View and create applications."""

  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  serializer_class = serializers.ApplicationPostSerializer

  def get(self, request, format=None):
    """View all of user's applications."""

    student = models.UserProfile.objects.get(id=self.request.user.id)
    applications = models.Applications.objects.filter(student=student)
    response = serializers.ApplicationSerializer(applications, many=True).data

    return Response(response, status=status.HTTP_200_OK)

  def post(self, request):
    """Create new application."""

    serializer = serializers.ApplicationPostSerializer(data=request.data)

    if serializer.is_valid():
      student = models.UserProfile.objects.get(id=self.request.user.id)
      tutor = models.UserProfile.objects.get(id=serializer.data['tutor_id'])
      application = models.Applications.objects.create(
        student=student,
        tutor=tutor,
      )
      response = serializers.ApplicationSerializer(application).data

      return Response(response, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
