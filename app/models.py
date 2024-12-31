from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField()
    pub_date = models.DateTimeField()
    notes = models.CharField(max_length=500)

    def __str__(self):
        return self.name
