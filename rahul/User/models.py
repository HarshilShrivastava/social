from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    IS_CUSTOMER=models.BooleanField(null=True,blank=True)