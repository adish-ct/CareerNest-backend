from django.db import models
from django.contrib.auth.models import User





# Create your models here.

# class Employer(models.Model):
#     employer = models.OneToOneField(User, on_delete=models.CASCADE)
#     employer_type = models.CharField(max_length=255, null=True, blank=True)
#     employer_description = models.TextField(null=True, blank=True)
#     employer_location = models.CharField(max_length=255, null=True, blank=True)
#     profile_image = models.ImageField(upload_to="employer/profile_images/" ,null=True, blank=True)
#     banner_image = models.ImageField(upload_to="employer/banner_images/" ,null=True, blank=True)
#     rating = models.IntegerField(default=5, blank=True)
#     is_verified = models.BooleanField(default=False)
#     avarage_salary = models.IntegerField(default=500000, blank=True)
#     role = models.CharField(default="Employer")
#     head_quarters = models.CharField(blank=True, null=True)
#     phone = models.CharField(max_length=10, null=True, blank=True)
#     followers = models.IntegerField(default=0, blank=True)
#     uuid = models.CharField(null=True, blank=True)
#     def __str__(self) -> str:
#         return self.employer.username



# class Candidate(models.Model):
#     candidate = models.OneToOneField(User, on_delete=models.CASCADE)
#     candidate_place = models.CharField(max_length=255, null=True, blank=True)
#     candidate_city = models.CharField(max_length=255, null=True, blank=True)
#     candidate_state = models.CharField(max_length=255, null=True, blank=True)
#     phone = models.CharField(max_length=10, blank=True, null=True)
#     profile_image = models.ImageField(upload_to="candidate/profile_images/", null=True, blank=True)
#     banner_image = models.ImageField(upload_to="candidate/banner_images/", null=True, blank=True)
#     designation = models.CharField(max_length=255, null=True, blank=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     resume = models.FileField(upload_to="candidate/resumes/", null=True, blank=True)
#     rating = models.IntegerField(default=5, blank=True)
#     uuid = models.CharField(null=True, blank=True) 



    
    

