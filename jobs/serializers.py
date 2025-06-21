from rest_framework import serializers
from jobs.models import JobApplication, JobPost

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields =  ['id', 'title', 'description', 'location', 'deadline', 'salary']
        # read_only_fields = ['recruiter','created_at']

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['candidate', 'job_post']