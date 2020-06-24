from django.db import models


class student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.first_name

# Create your models here.
