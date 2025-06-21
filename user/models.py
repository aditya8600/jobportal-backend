from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
        ROLE_CHOICES=(
            ('admin','Admin'),
            ('recruiter','Recruiter'),
            ('candidate','Candidate'),
        )
        
        role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='candidate')
        email = models.EmailField(unique=True)
        
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username']

def __str__(self):
        return self.email
    
class CandidateProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/',null=True,blank=True)
    experience = models.PositiveIntegerField(default=0)
    
    def __str__(self):
           return f"{self.user.email}'s Profile"

class RecruiterProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return f"{self.user.email}-{self.company_name}"
    
