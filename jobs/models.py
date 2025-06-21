from django.db import models
from django.conf import settings
from user.models import RecruiterProfile, CandidateProfile

class JobPost(models.Model):
    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role':'recruiter'}
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    location= models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True,blank=True )
    
    def __str__(self):
        return self.title
class JobApplication(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('shortlisted','Shortlisted'),
        ('rejected','Rejected'),
        ('hired','Hired'),    
    )
    
    candidate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role':'candidate'}
    )
    job_post = models.ForeignKey(JobPost,on_delete=models.CASCADE)
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.candidate.username} applied for {self.job_post.title}"