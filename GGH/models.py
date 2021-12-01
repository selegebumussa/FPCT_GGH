from django.db import models
from django.forms.widgets import Widget

# Create your models here.
class Membership(models.Model):
    Gender =[('M', 'Male'),('F', 'Female')]
    Baptised =[('Y', 'Yes'),('N', 'No')]
    Rescues=(('Y', 'Yes'),('N', 'No'))
    full_name  = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    physical_address = models.CharField(max_length=50)
    gender= models.CharField(choices=Gender, max_length=2)
    baptised =models.CharField(choices=Baptised, max_length=1)
    rescued_ggh = models.CharField(choices=Rescues, max_length=1)

class Equipment(models.Model):
    camera = models.IntegerField()
    computer = models.IntegerField()
    guitars = models.IntegerField()
    drums = models.IntegerField()
    microphones = models.IntegerField()
    speakers = models.IntegerField()
    keyboards = models.IntegerField()
    chairs= models.IntegerField()
    tables = models.IntegerField()
    stools = models.IntegerField()


class Post(models.Model):
    header_image = models.ImageField(upload_to ="media/")
    title = models.CharField(max_length=20, default='Event')
    




