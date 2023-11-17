from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from common.base_models import DateBaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("email required")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(email, password, **kwargs)
    

class Role(DateBaseModel):
    role = models.CharField(default="CANDIDATE", blank=True, null=True, unique=True)

    def __str__(self) -> str:
        return self.role


class User(DateBaseModel, AbstractUser):
    email = models.EmailField(unique=True, max_length=255, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username
    

class Profile(DateBaseModel, models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    about = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=5, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    place = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(upload_to="candidate/profile_images/", null=True, blank=True)
    banner_image = models.ImageField(upload_to="candidate/banner_images/", null=True, blank=True)
    employer_followers = models.IntegerField(default=0, blank=True)
    employer_description = models.TextField(null=True, blank=True)
    employer_avarage_salary = models.IntegerField(default=500000, blank=True)
    employer_head_quarters = models.CharField(blank=True, null=True)
    candidate_following = models.IntegerField(default=0, null=True)
    candidate_designation = models.CharField(max_length=255, null=True, blank=True)
    candidate_date_of_birth = models.DateField(null=True, blank=True)
    candidate_resume = models.FileField(upload_to="candidate/resumes/", null=True, blank=True) 