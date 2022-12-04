from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    fname=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    mob=models.BigIntegerField()
    dob=models.DateField()
    gender=models.CharField(max_length=10)
class Faculty(models.Model):
    name=models.CharField(max_length=30)
    fname=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    mob=models.BigIntegerField()
    dob=models.DateField()
    gender=models.CharField(max_length=10)
class Admin(models.Model):
    name=models.CharField(max_length=30)
    fname=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    mob=models.BigIntegerField()
    dob=models.DateField()
    gender=models.CharField(max_length=10)

# Create your models here.
