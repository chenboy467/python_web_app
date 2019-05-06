from django.db import models

# Create your models here.


class Person(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.lastName + ', ' + self.firstName


class LoginCredential(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return "self.username"
