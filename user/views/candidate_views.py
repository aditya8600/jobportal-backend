from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user.permissions import IsCandidate
from user.serializers.candidate_serializers import CandidateProfileSerializer
from user.models import CustomUser
from rest_framework import generics , permissions
from user.models import CandidateProfile

class CandidateOnlyView(APIView):
    permission_classes = [IsAuthenticated,IsCandidate]
    
    def get(self,request):
        return Response({'message':'Hello Candidate!!'})
    
    
class CandidateListCreateView(generics.ListCreateAPIView):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsCandidate]
        
    
class CandidateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset =CandidateProfile.objects.all()    
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated,IsCandidate]
    lookup_field = 'id'