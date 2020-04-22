from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from User.models import (
    User
)

class Profile(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    Name=models.CharField( max_length=50)
    Website=models.URLField( max_length=200,null=True)
    Bio=models.TextField(null=True)
    Email=models.EmailField( max_length=254)
    Phone_Number=PhoneNumberField()
    Gender=models.BooleanField(null=True)
    Private=models.BooleanField()
    profile_pic=models.ImageField( upload_to="media/profilw_pic",null=True)

class Status(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    TextField=models.TextField(null=True,blank=True)
    Descreption=models.TextField(null=True,blank=True)
    ImageField=models.ImageField(upload_to="media/status/Image",null=True,blank=True)
    VideoFields=models.FileField(upload_to="media/status/video",null=True,blank=True)
    Timestamp=models.DateTimeField(auto_now_add=True)
    