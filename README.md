This is the backend API for a Job Portal Web Application built with Django and Django REST Framework (DRF). It handles authentication, job posting, job applications, and role-based access control for Admin, Recruiter, and Candidate users.

 Project Structure
jobportal-backend/
│
├── jobportal/              # Project settings and URLs
├── jobs/                   # Job posting and application logic
├── user/                   # User authentication and roles
├── requirements.txt        # Python dependencies
├── db.sqlite3              # Default development database
└── render.yaml             # Configuration for Render deployment

Roles & Features

1.Admin
Can view overall platform data (future scope)

2.Recruiter
Register/Login
Create, update, and delete job posts
View applications for posted jobs

3.Candidate
Register/Login
Browse jobs
Apply to jobs
Track application status

 Setup Instructions
1. Install Dependencies
pip install -r requirements.txt
2.  Apply Migrations
python manage.py makemigrations
python manage.py migrate
3.  Create Superuser (Admin)
python manage.py createsuperuser
4.  Run Server
python manage.py runserver
API will be live at: http://localhost:8000/

 Authentication
Uses JWT (JSON Web Tokens) for secure login and protected routes.

POST /api/token/ – Get access and refresh tokens

POST /api/token/refresh/ – Refresh token

POST /api/logout/ – Logout

Tokens must be sent in the header:
Authorization: Bearer <access_token>


API Endpoints
Method	Endpoint	Description
POST	/api/register/	Register (any role)
POST	/api/token/	Login (JWT)
GET	/api/me/	Get current user
GET	/api/jobs/	Public job listings
POST	/api/jobs/<id>/apply/	Apply for a job (Candidate)
GET	/api/my-applications/	Candidate's applications
GET	/api/recruiter/jobposts/	Recruiter's job posts
POST	/api/recruiter/jobposts/create/	Create job post (Recruiter)

Deployment
App is configured for deployment using Render with render.yaml.

To deploy:
Push code to GitHub
Connect Render and set up a Web Service
Add environment variables:

DEBUG=False
SECRET_KEY=your-secret-key

Add Build & Start command:
pip install -r requirements.txt
gunicorn jobportal.wsgi:application
License
This project is licensed under the MIT License.