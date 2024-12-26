from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=256) 
    task_date = models.DateField(auto_now_add=True)