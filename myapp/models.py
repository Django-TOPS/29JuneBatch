from django.db import models

# Create your models here.

class signup_master(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.IntegerField()

class userform(models.Model):
    title=models.CharField(max_length=100)
    option=models.CharField(max_length=100)
    select_file=models.FileField(upload_to='MyFiles')
    disc=models.TextField()
