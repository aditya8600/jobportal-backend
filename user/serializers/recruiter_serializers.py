from rest_framework import serializers
from user.models import RecruiterProfile
from jobs.models import JobPost

class RecruiterProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username',read_only = True)
    email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = RecruiterProfile
        fields = ['id','username','email','company_name','position']
        read_only_fields = ['id','username','email']
        
class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['id', 'title', 'description', 'location',] 
        read_only_fields = ['id','recruiter','created_at']        