from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     phone_number = models.CharField(max_length=20)

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    job_title = models.CharField(max_length=100)
    salary = models.FloatField(max_length=50)

    class Meta:
        db_table = "employee"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    profile_photo = CloudinaryField("image",null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        ordering = ['-pk']
    
    