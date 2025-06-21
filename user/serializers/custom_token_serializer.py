from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['role']=user.role
        return token
    def validate(self, attrs):
        data = super().validate(attrs)
        data['email']=self.user.email
        data['role']=self.user.role
        return data