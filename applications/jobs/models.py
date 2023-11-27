from django.db import models
from common.base_models import DateBaseModel
from applications.accounts.models import User

# Create your models here.

class Jobs(DateBaseModel):
    employer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    job_role = models.CharField(max_length=255, blank=True, null=True)
    job_location = models.CharField(max_length=255, blank=True, null=True)
    job_ctc = models.IntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=255, null=True, blank=True)
    experience = models.IntegerField(default=0, blank=True)
    work_type = models.CharField(max_length=255, null=True, blank=True)
    vaccancy = models.IntegerField(default=1, blank=True)
    skills = models.CharField(max_length=300, blank=True, null=True)
    qualifications = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    job_id = models.CharField(max_length=255, blank=True)
    application_count = models.IntegerField(default=0, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True)
    highlight = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.job_role} - {self.employer.username}'