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
class CommentManager(models.Manager):
    def all(self):
        qs=super(CommentManager,self).filter(parent=None)
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(
            content_type=content_type, object_id=obj_id
        ).filter(parent=None)
        return qs

class Comment(models.Model):
    Post=models.ForeignKey(Post, on_delete=models.CASCADE)
    Profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    Comment=models.TextField()
    Timestamp=models.DateTimeField( auto_now_add=True)
    Parent = models.ForeignKey("self", null=True, blank=True,related_name='reply_set', on_delete=models.PROTECT)
    #objects = CommentManager()

    class meta:
        ordering = ["-timestamp"]


    def children(self):
        return comments.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True



class CommentLike(models.Model):
    Comment=models.ForeignKey(Comment, on_delete=models.CASCADE)
    Profile=models.OneToOneField(Profile, on_delete=models.CASCADE)