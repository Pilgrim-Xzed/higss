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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(help_text='Enter email address')
    timestamp = models.DateTimeField()
    passport = models.ImageField(upload_to='passports/', blank=True, null=True)
    surname_of_pupil = models.CharField(max_length=255, help_text='Enter surname of pupil')
    firstname_of_pupil = models.CharField(max_length=255, help_text='Enter firstname of pupil')
    othername_of_pupil = models.CharField(max_length=255, help_text='Enter othername of pupil', null=True, blank=True)
    sex = models.CharField(choices=GENDER_CHOICES, max_length=128, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    class_applying_to = models.CharField(choices=CLASS_CHOICES, max_length=128, null=True, blank=True)
    full_name_of_guardian = models.CharField(max_length=50)
    relationship_with_pupil = models.CharField(choices=RELATIONSHIP_CHOICES, max_length=128)
    profession = models.CharField(max_length=50, null=True, blank=True)
    residential_address = models.CharField(max_length=50, null=True, blank=True)
    office_address = models.CharField(max_length=50, null=True, blank=True)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    child_aliments = models.TextField(help_text='Does the child have any persistent aliments?', null=True, blank=True)
    confirm = models.BooleanField(default=False)
    admission_number = models.CharField(null=True, blank=True, max_length=50)
    school_fees = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.surname_of_pupil +' '+ self.firstname_of_pupil