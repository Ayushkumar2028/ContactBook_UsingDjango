from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE,null=True, blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    note = models.CharField(max_length=200)


def __str__(self):
    return self.name
