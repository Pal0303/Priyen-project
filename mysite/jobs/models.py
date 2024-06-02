from django.db import models

class Job(models.Model):

    def __str__(self):
        return self.Designation

    Designation = models.CharField(max_length=100)
    Description = models.CharField(max_length = 2000)
    Experience = models.CharField(max_length=100)
    Skills = models.CharField(max_length=500)

class Applicant(models.Model):
    resume = models.FileField(upload_to='jobs/pdfs')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    matching_skills = models.CharField(max_length=200)

class question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000)

class answer(models.Model):
    answer1 = models.CharField(max_length=1000, default='')
    answer2 = models.CharField(max_length=1000, default='')
    answer3 = models.CharField(max_length=1000, default='')
    answer4 = models.CharField(max_length=1000, default='')
    answer5 = models.CharField(max_length=1000, default='')

class Result(models.Model):
    Designation = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    score = models.IntegerField(max_length=10)

    # models.py

from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        email = models.EmailField()
        # Add other candidate fields as needed...

class Company(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        industry = models.CharField(max_length=100)
        # Add other company fields as needed...

class Query(models.Model):
        user_type_choices = [('candidate', 'Candidate'), ('company', 'Company')]
        user_type = models.CharField(max_length=10, choices=user_type_choices)
        user_id = models.IntegerField()
        message = models.TextField()
        timestamp = models.DateTimeField(auto_now_add=True)
        # Add any other fields as needed...


