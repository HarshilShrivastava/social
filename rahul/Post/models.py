from django.db import models
from Profile.models import(
    Profile
)
# Create your models here.
class Post(models.Model):
    Profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    Title=models.CharField( max_length=255)
    Description=models.TextField(blank=True)
    Image=models.ImageField( upload_to='media/Post/',null=True,blank=True)
    Video=models.FileField(upload_to='media/video/', max_length=100,null=True,blank=True)
    Timestamp=models.DateTimeField( auto_now_add=True)

class Like(models.Model):
    Post=models.ForeignKey(Post, on_delete=models.CASCADE)
    Profile=models.OneToOneField(Profile, on_delete=models.CASCADE)

class Comment(models.Model):
    Post=models.ForeignKey(Post, on_delete=models.CASCADE)
    Profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    Comment=models.TextField()
    Timestamp=models.DateTimeField( auto_now_add=True)