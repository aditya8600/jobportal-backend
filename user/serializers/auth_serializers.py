from rest_framework import serializers
from user.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['email','password','role']
        extra_kwargs = {
            'password':{'write_only':True}
        }
        
    def create(self,validated_data):
        email = validated_data['email']
        username=email.split('@')[0]
        user = CustomUser.objects.create_user(
                email=email,
                username=username,
                password=validated_data['password'],
                role = validated_data.get('role','candidate')
   
            )
        return user