from django.urls import path
from user.views.auth_views import RegisterView , LogoutView 
from user.views.admin_views import AdminOnlyView
from user.views.candidate_views import CandidateOnlyView, CandidateListCreateView, CandidateRetrieveUpdateDestroyView
from user.views.recruiter_views import RecruiterOnlyView , RecruiterListCreateView,RecruiterRetrieveUpdateDestroyView, RecruiterJobPostListCreateView, RecruiterJobPostRetrieveUpdateDestroyView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('token/refresh/',TokenRefreshView.as_view(),name='refresh'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('dashboard/admin/',AdminOnlyView.as_view(),name='admin-dashboard'),
    path('dashboard/recruiter/',RecruiterOnlyView.as_view(),name='recruiter-dashboard'),
    path('candidate/dashboard/',CandidateOnlyView.as_view(),name='candidate-dashboard'),
    path('candidates/',CandidateListCreateView.as_view(),name = 'candidate-list-create'),
    path('candidates/<int:id>/',CandidateRetrieveUpdateDestroyView.as_view(),name='candidate-detail'),
    path('recruiters/',RecruiterListCreateView.as_view(),name='recruiter-list-create'),
    path('recruiters/<int:id>/',RecruiterRetrieveUpdateDestroyView.as_view(),name='recruiter-detail'),
    path('recruiter/jobposts/',RecruiterJobPostListCreateView.as_view(),name='recruiter-jobpost-list-create'),
    path('recruiter/jobposts/<int:id>/',RecruiterJobPostRetrieveUpdateDestroyView.as_view(),name='recruiter-jobpost-details')
]
