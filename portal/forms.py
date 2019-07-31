from django.forms import ModelForm,DateField,DateInput,FileInput
from django import forms
from .models import Application
from django.utils.translation import ugettext_lazy as _

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'date_of_birth':DateInput(attrs={'type':'date','class':'datetimepicker-dummy-input','readonly':'readonly'}),
            'passport':FileInput(attrs={'class':'file-input'})
        }
        labels = {
            'passport':_("Pupil's Picture &nbsp;&nbsp;&nbsp;"),
            'firstname_of_pupil':_("First Name of Pupil"),
            'surname_of_pupil':_("Surname of Pupil"),
            'othername_of_pupil':_("Middle Name of Pupil"),
            'sex':_("Gender"),
            'date_of_birth':_("Date of Birth"),
            'class_applying_to':_("Class Applying to"),
            'full_name_of_guardian':_("Full Name of Sponsor"),
            'relationship_with_pupil':_("Relationship with Pupil")
        }

        exclude = ('user', 'passed', 'timestamp', 'admission_number')

class CheckForm(forms.Form):
    admission_number = forms.CharField(max_length=50)