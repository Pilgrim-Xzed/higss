from django.db import models
from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

CLASS_CHOICES = (
   ('JSS1', 'JSS1'),
   ('JSS2', 'JSS2'),
   ('JSS3', 'JSS3'),
   ('SSS1', 'SSS1'),
   ('SSS2', 'SSS2'),
   ('SSS3', 'SSS3')
)

RELATIONSHIP_CHOICES = (
    ('Father', 'Father'),
    ('Mother', 'Mother'),
    ('Guardian', 'Guardian')
)

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    passport = models.ImageField(upload_to='passports/')
    surname_of_pupil = models.CharField(max_length=255)
    firstname_of_pupil = models.CharField(max_length=255)
    othername_of_pupil = models.CharField(max_length=255)
    sex = models.CharField(choices=GENDER_CHOICES, max_length=128)
    date_of_birth = models.DateField()
    class_applying_to = models.CharField(choices=CLASS_CHOICES, max_length=128)
    full_name_of_guardian = models.CharField(max_length=50)
    relationship_with_pupil = models.CharField(choices=RELATIONSHIP_CHOICES, max_length=128)
    profession = models.CharField(max_length=50)
    residential_address = models.CharField(max_length=50)
    office_address = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    child_aliments = models.TextField(help_text='Does the child have any persistent aliments?')
    passed = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name_of_pupil