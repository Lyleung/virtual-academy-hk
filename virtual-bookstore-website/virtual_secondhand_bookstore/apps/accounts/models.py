from django.db import models
from django.contrib.auth.models import User


# User also has persona, like DIYer, system administrator, hacker
# it is system generated
# means I can generate the User persons as website administrator
# but none of the persons can assign

#  Interests = request.user.profile.interests.all()

class UserInterest(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalised_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalised_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
class UserProfile(models.Model):
    # owner foreign key
    # if the user is deletes, it will cascade all other table to delete
    # when we have our user reference from out request side user
    # we can reference the profile by typing dot profile
    # related_name="profile" means it can pass from "import User" to request.user.profile

    # owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # defines the views of model

    # settings
    is_full_name_displayed = models.BooleanField(default=True)
    # details
    # short description for user
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    # only I can add or remove persona from persona table
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)
    interests = models.ManyToManyField(UserInterest, blank=True)
