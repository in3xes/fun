from django.db import models

# Create your models here.

class prof(models.Model):
    name = models.CharField(max_length=200)
    institute = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
