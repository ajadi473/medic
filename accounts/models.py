from django.db import models

# Create your models here.
class accounts_patientmodel(models.Model):
    email = models.CharField(max_length=100, help_text='Enter your email address')
    name = models.CharField(max_length=200, null=True, unique=True)
    password = models.CharField(max_length=200, null=True)
    address = models.TextField(max_length=800, null=True)
    dob = models.DateTimeField(null=True)
    nationality = models.CharField(max_length=200, null=True, unique=True)
    place_of_birth = models.CharField(max_length=200, null=True, unique=True)
    diseased = models.CharField(max_length=200, null=True, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    
    def __str___(self):
        return self.name

