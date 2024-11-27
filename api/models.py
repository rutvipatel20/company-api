from django.db import models

# Create your models here.

#Company Model

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=((1,'IT'),(2,'Non IT'),(3,'Other')))
    created_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

# Employee Model
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=((1,'Manager'),(2,'Software Developer'),(3,'HR')))
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)