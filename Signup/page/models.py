from django.db import models

# Create your models here.
class Signup(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    EmailAddress = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return self.EmailAddress
