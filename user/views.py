from django.shortcuts import render
from rest_framework import generics
from .serializers.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .permissions import IsAdmin, IsCandidate, IsRecruiter


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
        
class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]     
    
    def get(self,request):
        return Response({'message': "Hello Admin!!"})
    
class RecruiterOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsRecruiter]     
    
    def get(self,request):
        return Response({'message': "Hello Recruiter!!"})
    
class CandidateOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsCandidate]     
    
    def get(self,request):
        return Response({'message': "Hello Candidate!!"})
    
      