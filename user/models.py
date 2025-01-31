from django.db import models

# Create your models here.
class userregistermodel(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    profile_pic = models.FileField()
    voter_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)