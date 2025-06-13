from rest_framework import serializers
from user.models import CandidateProfile, CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','email','firstname','lastname']

class CandidateProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = CandidateProfile
        fields = ['id','user','resume','experience']
        
        