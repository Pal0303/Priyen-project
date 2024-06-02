# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logincandidate/', views.logincandidate, name='login'),
    path('employer/login/', views.employer_login, name='employer_login'),
    # Add URLs for applicant_login and employer_login if needed
]
