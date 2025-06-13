from django.urls import path
from jobs.views import (
    JobApplicationCreateView,
    CandidateJobApplicationListView, RecruiterJobApplicationListView,UpdateJobApplicationStatusView,RecruiterJobPostCreateView,RecruiterJobPostDeleteView,RecruiterJobPostListView,RecruiterJobPostUpdateView,PublicJobPostListView,PublicJobPostDetailView
)

urlpatterns = [
    path('jobs/<int:job_id>/apply/', JobApplicationCreateView.as_view(), name='apply-job'),
    path('my-applications/', CandidateJobApplicationListView.as_view(), name='my-applications'),
    path('recruiter/applications/',RecruiterJobApplicationListView.as_view(),name='recruiter-aplications'),
    path('recruiter/applications/<int:id>/',UpdateJobApplicationStatusView.as_view(),name='update-application-status'),
     path('recruiter/jobposts/', RecruiterJobPostListView.as_view(), name='recruiter-jobpost-list'),
    path('recruiter/jobposts/create/', RecruiterJobPostCreateView.as_view(), name='recruiter-jobpost-create'),
    path('recruiter/jobposts/<int:id>/update/', RecruiterJobPostUpdateView.as_view(), name='recruiter-jobpost-update'),
    path('recruiter/jobposts/<int:id>/delete/', RecruiterJobPostDeleteView.as_view(), name='recruiter-jobpost-delete'),
    path('jobs/', PublicJobPostListView.as_view(), name='public-job-list'),
    path('jobs/<int:id>/', PublicJobPostDetailView.as_view(), name='public-job-detail'),
]


