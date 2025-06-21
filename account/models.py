from django.db import models

# Create your models here.
class save_otp(models.Model):
    username = models.CharField(max_length=100)
    otp = models.IntegerField(max_length=10)