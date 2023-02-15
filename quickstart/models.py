from django.db import models


# Create your models here.

class Student(models.Model):
    GENDERCHOICE = (
        ('male', 'male'),
        ('female', 'female'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255, choices=GENDERCHOICE)

