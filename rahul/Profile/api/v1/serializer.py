from rest_framework import serializers 
from Profile.models import (
    Profile,
    Status
)
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        exclude = ('id','User', )
class ProfileReadSerializer(serializers.ModelSerializer):
    Username=serializers.SerializerMethodField('get_username')

    class Meta:
        model=Profile
        fields = ['Username','Name','Website','Bio','Email','Phone_Number','Gender','Private','profile_pic']
    def get_username(self,info):
        data=info.User.username
        return data

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model=Status
        fields = ['TextField','Descreption','ImageField','VideoFields' ]

class StatusReadSerializer(serializers.ModelSerializer):

    class Meta:
        model=Status
        fields = '__all__' 