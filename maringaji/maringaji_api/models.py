from django.db import models

from django.contrib.auth.models import BaseUserManager # Allows us to alter behaviour of creating UserProfiles

from django.contrib.auth.models import AbstractBaseUser # Base user that we are going to modify
from django.contrib.auth.models import PermissionsMixin # Allows us to easily set up user permissions

# Create your models here.

class UserProfileManager(BaseUserManager):

  def create_user(self, email, name, is_tutor, is_student, desc, password=None):
    if not email:
      raise ValueError('Users must have an email address.')

    email = self.normalize_email(email)
    user = self.model(
      email=email,
      name=name,
      is_tutor=is_tutor,
      is_student=is_student,
      desc=desc
      )

    user.set_password(password) # uses encryption and hashing, bcrypt
    user.save(using=self._db)

    return user

  def create_superuser(self, email, name, password):

    user = self.create_user(email, name, False, False, None, password)
    user.is_superuser = True # allows user to have privileges in Django Admin
    user.is_staff = True # allows user to have privileges in Django Admin
    user.save(using=self._db)
    return user

 
class UserProfile(AbstractBaseUser, PermissionsMixin):

  # More about Django models: https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.Field

  email = models.EmailField(unique=True)
  name = models.CharField(max_length=50)
  is_tutor = models.BooleanField(default=False)
  is_student = models.BooleanField(default=False)
  desc = models.TextField(null=True, blank=True)
  is_active = models.BooleanField(default=True) # must-have attribute
  is_staff = models.BooleanField(default=False) # must-have attribute

  objects = UserProfileManager()

  USERNAME_FIELD = 'email' # replace Django's default behaviour of using a separate username
  REQUIRED_FIELDS = ['name'] # email is already required

  def get_full_name(self):
    """Get user's full name."""

    return self.name

  def get_short_name(self):
    """Get user's short name."""

    return self.name

  def __str__(self):
    """A string representation of the UserProfile object."""

    return self.email


class Applications(models.Model):
  """A student's application for a tutor."""

  application_id = models.AutoField(primary_key=True)
  student = models.ForeignKey(UserProfile, related_name='student')
  tutor = models.ForeignKey(UserProfile, related_name='tutor')
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    """A string representation of the Application object."""

    return '{0} + {1}'.format(self.student.name, self.tutor.name)