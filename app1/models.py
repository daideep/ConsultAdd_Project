from django.db import models

# Create your models here.

class Signup(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    session = models.ForeignKey('Session', on_delete=models.PROTECT)

    def __str__(self):
        return self.name




