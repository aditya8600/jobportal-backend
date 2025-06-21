from rest_framework import serializers
from user.models import CustomUser



class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('email','password','role')
        extra_kwargs = {
            'password':{'write_only':True}
        }
        
    def create(self, validated_data):
        
        return CustomUser.objects.create_user(
            username=validated_data['email']
            email=validated_data['email']
            password=validated_data['password']
            role=validated_data['role']
        )