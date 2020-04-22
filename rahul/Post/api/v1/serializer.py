from rest_framework import serializers 
from Post.models import (
    Post,
    Like,
    Comment
)
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        exclude=('id','Profile','Timestamp','Archived')

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
        fields=['Comment','Parent']

class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommentReadSerializer(serializers.ModelSerializer):
    reply_set = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'Timestamp', 'Comment', 'Parent', 'reply_set')