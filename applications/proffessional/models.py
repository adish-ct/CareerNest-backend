from django.db import models
from common.base_models import DateBaseModel
from applications.accounts.models import User

# Create your models here.

class Experience(DateBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    job_role = models.CharField(max_length=255, null=True, blank=True)
    organization = models.CharField(max_length=255, null=True, blank=True)
    job_type = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    work_type = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False, blank=True)
    time_period = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    skills = models.TextField(max_length=500, blank=True, null=True)
    documents = models.FileField(upload_to='documents/', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user} + {self.job_role}'
    


class Education(DateBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    stream = models.CharField(max_length=255, null=True, blank=True)
    organization = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    course_type = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    duration = models.CharField(max_length=255, null=True, blank=True)
    currently_studying = models.BooleanField(default=False, blank=True)
    score = models.IntegerField(default=5, blank=True)
    documents = models.FileField(upload_to='documents/', null=True, blank=True)
    
    
    def __str__(self) -> str:
        return f'{self.user.username} - {self.stream}'
    


class Project(DateBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    project_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=300, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False, blank=True)
    collab_project = models.BooleanField(default=False, blank=True)
    git_link = models.CharField(null=True, blank=True)
    website_link = models.CharField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    challenges = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.project_name}'
    

    
    



    
    

