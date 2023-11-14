from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Employer(models.Model):
    employer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    employer_type = models.CharField(max_length=255, null=True, blank=True)
    employer_description = models.TextField(null=True, blank=True)
    employer_location = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    banner_image = models.ImageField(null=True, blank=True)
    rating = models.IntegerField(default=5, blank=True)
    is_verified = models.BooleanField(default=False)
    avarage_salary = models.IntegerField(default=500000, blank=True)
    role = models.CharField(default="Employer")
    head_quarters = models.CharField(blank=True, null=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    followers = models.IntegerField(default=0, blank=True)

    def __str__(self) -> str:
        return self.employer.username
    



    

