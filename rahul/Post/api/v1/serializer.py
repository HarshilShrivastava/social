from rest_framework import serializers 
from Post.models import (
    Post,
    Like,
    Comment
)
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        exclude=('id','Profile','Timestamp')

class PostReadSerializer(serializers.ModelSerializer):
    selfProfile=serializers.SerializerMethodField('get_username')
    class Meta:
        model=Post
        fields=['selfProfile','Title','Description','Image','Video','Timestamp','id']
    def get_username(self,info):
        data=info.Profile.User.username
        return data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['Comment']

class CommentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
