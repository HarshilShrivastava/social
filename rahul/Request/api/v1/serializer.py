from Request.models import (
    Request,
    Confirmed
)
from rest_framework import serializers 
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Request
        fields=['From','To']


class  ConfirmedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Confirmed
        fields=['Receiver','Sender']

class  ConfirmedReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Confirmed
        fields='__all__'
        

class RequestReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Request
        fields='__all__'
