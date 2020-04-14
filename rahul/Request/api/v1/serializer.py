from Request.models import (
    Request,
    Confirmed
)
from rest_framework import serializers 
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Request
        fields=['From','To']
class RequestDSerializer(serializers.ModelSerializer):
    class Meta:
        model=Request
        fields=['From','To']

class  ConfirmedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Confirmed
        fields=['Receiver','Sender']

class  ConfirmedReadSerializer(serializers.ModelSerializer):
    Sender_name=serializers.SerializerMethodField('get_sender_name')
    receiver_name=serializers.SerializerMethodField('get_receiver_name')
    class Meta:
        model=Confirmed
        fields=['Sender','Receiver','Timestamp','id','receiver_name','Sender_name']
    def get_sender_name(self,info):
        data=info.Sender.Name
        return data
    def get_receiver_name(self,info):
        data=info.Sender.Name
        return data

class RequestReadSerializer(serializers.ModelSerializer):
    From_name=serializers.SerializerMethodField('get_From_name')
    To_name=serializers.SerializerMethodField('get_To_name')
    class Meta:
        model=Request
        fields=['created','To','From','From_name','To_name']
    def get_From_name(self,info):
        data=info.From.Name
        return data
    def get_To_name(self,info):
        data=info.To.Name
        return data
