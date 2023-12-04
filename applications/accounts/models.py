from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager, AbstractBaseUser
from common.base_models import DateBaseModel


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
    

class Role(DateBaseModel):
    role = models.CharField(default="CANDIDATE", blank=True, null=True, unique=True)

    def __str__(self) -> str:
        return self.role



class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    phone = models.CharField(max_length=12, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()

    def __str__(self):
        return self.username

class Profile(DateBaseModel, models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    additional_email = models.EmailField(blank=True, null=True)
    about = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=5, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    place = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=6, blank=True, null=True)
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    banner_image = models.ImageField(upload_to="banner_images/", null=True, blank=True)
    organization = models.CharField(max_length=25, null=True, blank=True)
    employer_followers = models.IntegerField(default=0, blank=True)
    employer_description = models.TextField(null=True, blank=True)
    employer_avarage_salary = models.IntegerField(default=500000, blank=True)
    employer_head_quarters = models.CharField(blank=True, null=True)
    candidate_following = models.IntegerField(default=0, null=True)
    candidate_designation = models.CharField(max_length=255, null=True, blank=True)
    candidate_date_of_birth = models.DateField(null=True, blank=True)
    candidate_resume = models.FileField(upload_to="resumes/", null=True, blank=True) 
    candidate_expecting_salary = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username