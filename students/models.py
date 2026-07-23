from django.db import models
from django.conf import settings

class Department(models.Model):
    name = models.CharField(max_length=100)
    building = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model): 
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):  
    GENDER_CHOICES = ( 
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    photo = models.ImageField(upload_to='students/', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    courses = models.ManyToManyField(Course, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name()
