from rest_framework import serializers 
from Profile.models import Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['Phone_Number']