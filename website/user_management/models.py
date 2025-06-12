from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    pronouns = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField()
    bio = models.CharField(max_length=200, null=True, blank=True)