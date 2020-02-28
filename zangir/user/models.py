from django.db import models
from django.contrib.auth.models import AbstractUser

class ZangirUser(AbstractUser):
    mobile = models.CharField(max_length=30, blank=True)


