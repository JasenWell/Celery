from django.db import models

# Create your models here.


class Add(models.Model):
    task_id = models.CharField(max_length=256)
    first = models.IntegerField()
    second = models.IntegerField()
    log_date = models.DateTimeField(auto_now=True)
