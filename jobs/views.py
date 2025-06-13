from rest_framework import generics, permissions
from jobs.models import JobApplication, JobPost
from jobs.serializers import JobApplicationSerializer, JobPostSerializer
from user.permissions import IsCandidate
from user.permissions import IsRecruiter

class JobApplicationCreateView(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsCandidate]

    def perform_create(self, serializer):
        job_id = self.kwargs.get('job_id')
        job = JobPost.objects.get(id=job_id)
        serializer.save(candidate=self.request.user, job=job)


class CandidateJobApplicationListView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsCandidate]

    def get_queryset(self):
        return JobApplication.objects.filter(candidate=self.request.user)

class RecruiterJobApplicationListView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes=[permissions.IsAuthenticated,IsRecruiter]
    
    def get_queryset(self):
        return JobApplication.objects.filter(job__recruiter=self.request.user)
    
class UpdateJobApplicationStatusView(generics.UpdateAPIView):
    queryset= JobApplication.objects.all()
    serializer_class=JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated,IsRecruiter]
    lookup_field ='id'
    
    def get_queryset(self):
        return JobApplication.objects.filter(job__recruiter=self.request.user)    
    
class JobPostCreateView(generics.CreateAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]
    
    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)
        
class RecruiterJobPostListView(generics.ListAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]  
    
    
    def get_queryset(self):
        return JobPost.objects.filter(recruiter=self.request.user)      
    
class JobPostUpdateView(generics.UpdateAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]
    lookup_field = 'id'

    def get_queryset(self):
        return JobPost.objects.filter(recruiter=self.request.user)

class JobPostDeleteView(generics.DestroyAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]
    lookup_field = 'id'

    def get_queryset(self):
        return JobPost.objects.filter(recruiter=self.request.user)

class PublicJobListView(generics.ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [permissions.AllowAny]    
        
class RecruiterJobPostCreateView(generics.CreateAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)


class RecruiterJobPostListView(generics.ListAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]

    def get_queryset(self):
        return JobPost.objects.filter(recruiter=self.request.user)


class RecruiterJobPostUpdateView(generics.UpdateAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]
    lookup_field = 'id'

    def get_queryset(self):
        return JobPost.objects.filter(recruiter=self.request.user)


class RecruiterJobPostDeleteView(generics.DestroyAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]
    lookup_field = 'id'

    def get_queryset(self):
        return JobPost.objects.filter(recruiter=self.request.user)        
    
class PublicJobPostListView(generics.ListAPIView):
    queryset = JobPost.objects.all().order_by('-created_at')
    serializer_class = JobPostSerializer
    permission_classes = [permissions.AllowAny]


class PublicJobPostDetailView(generics.RetrieveAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    lookup_field = 'id'
    permission_classes = [permissions.AllowAny]
    
        