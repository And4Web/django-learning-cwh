from django.db import models

# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=150)
  phone = models.CharField(max_length=20)  
  desc = models.TextField(max_length=1000)
  created_at = models.DateField()
