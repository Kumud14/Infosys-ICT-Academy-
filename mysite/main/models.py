from django.db import models

# Define your model
class Test(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()

class Task(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title