from rest_framework.views import APIView
from rest_framework.response import Response
from user.permissions import IsRecruiter
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,permissions
from user.models import RecruiterProfile
from user.serializers.recruiter_serializers import RecruiterProfileSerializer
from user.permissions import IsRecruiter
from jobs.models import JobPost
from user.serializers.recruiter_serializers import JobPostSerializer


class RecruiterOnlyView(APIView):
    permission_classes = [IsAuthenticated,IsRecruiter]
    
    def get(self,request):
        return Response({'message':'Hello Recruiter!!'})
    
class RecruiterListCreateView(generics.ListCreateAPIView):
    queryset = RecruiterProfile.objects.all()
    serializer_class = RecruiterProfileSerializer
    permission_classes = [IsAuthenticated,IsRecruiter] 
    lookup_field = 'id'
    
class RecruiterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecruiterProfile.objects.all()
    serializer_class=RecruiterProfileSerializer
    permission_classes=[IsAuthenticated,IsRecruiter]
    lookup_field='id'   
    
class RecruiterJobPostListCreateView(generics.ListCreateAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated,IsRecruiter] 
    
    def get_queryset(self):
        return JobPost.objects.filter(recruiter=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(recruiter=self.request.user)  
        
        
class RecruiterJobPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated,IsRecruiter]
    lookup_field = 'id'
    
    def get_queryset(self):
        return JobPost.objects.filter(recruiter=self.request.user)   