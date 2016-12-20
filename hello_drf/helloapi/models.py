from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)


    def __unicode__(self):
        return self.name
