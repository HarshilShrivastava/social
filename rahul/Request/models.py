from django.db import models
from django.utils import timezone

# Create your models here.
from Profile.models import(
    Profile
)
class Request(models.Model):
    From = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="From")
    To = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="To")
    created = models.DateTimeField(default=timezone.now)
    viewed = models.DateTimeField(blank=True, null=True)
    

class Confirmed(models.Model):
    Sender = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="Sender")
    Receiver = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="Receiver")
    Timestamp= models.DateTimeField(blank=True, null=True)

