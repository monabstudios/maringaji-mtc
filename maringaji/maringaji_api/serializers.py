from rest_framework import serializers

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
  """A serializer for our User Profile objects."""

  class Meta:
    model = models.UserProfile
    fields = (
      'id',
      'email',
      'name',
      'desc',
      'is_tutor',
      'is_student',
      'password',
    )
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    """Create a return a new user."""

    user = models.UserProfile(
      email=validated_data['email'],
      name=validated_data['name'],
      desc=validated_data['desc'],
      is_tutor=validated_data['is_tutor'],
      is_student=validated_data['is_student'],
    )
    user.set_password(validated_data['password'])
    user.save()

    return user