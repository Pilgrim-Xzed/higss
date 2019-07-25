from django.forms import ModelForm,DateField,DateInput,FileInput
from django import forms
from .models import Application

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'date_of_birth':DateInput(attrs={'type':'date','class':'datetimepicker-dummy-input','readonly':'readonly'}),
            'passport':FileInput(attrs={'class':'file-input'})
        }

        exclude = ('user', 'passed', 'timestamp', 'admission_number')

class CheckForm(forms.Form):
    admission_number = forms.CharField(max_length=50)