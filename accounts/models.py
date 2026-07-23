from tokenize import blank_re

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES=(
        ('ADMIN','Admin'),
        ('STUDENT','Student'),
        ('TEACHER','Teacher')
    )

    phone=models.CharField(max_length=20,blank=True)

    profile_picture=models.ImageField(upload_to='profile_pictures',blank=True,null=True)

    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default='STUDENT')

    def __str__(self):
        return self.username