from django.db import models

# Create your models here.

class prof(models.Model):
    INSTITUTE_CHOICES = (
        ('IITB', 'IIT Bombay'),
        ('IITD', 'IIT Delhi'),
        ('IITK', 'IIT Kanpur'),
        ('IITG', 'IIT Kharagpur'),
        ('IITM', 'IIT Madras'),
        ('IITR', 'IIT Roorkee'),
        ('IITW', 'IIT Guwahati'),
        )

    DEPT_CHOICES = (
        ('MAT', 'Mathematics'),
        ('CHM', 'Chemistry'),
        ('PHY', 'Physics'),
        )

    coolness = (
        ('a', 'Worst'),
        ('b', 'Not Okay'),
        ('c', 'Ok Ok'),
        ('d', 'Cool'),
        ('e', 'Ultra Cool'),
        )

    name = models.CharField(max_length=200)
    institute = models.CharField(max_length=4, choices=INSTITUTE_CHOICES)
    department = models.CharField(max_length=3, choices=DEPT_CHOICES)
    website = models.CharField(max_length=200)
    email = models.EmailField(max_length=20)
    photo = models.ImageField(upload_to='images')
    coolness = models.IntegerField()
    knowledge = models.IntegerField()
    looks = models.IntegerField()

    def __unicode__(self):
        return self.name
