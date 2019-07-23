from django.forms import ModelForm,DateField,DateInput,FileInput
from .models import Application

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'date_of_birth':DateInput(attrs={'type':'date','class':'datetimepicker-dummy-input','readonly':'readonly'}),
            'passport':FileInput(attrs={'class':'file-input'})
        }

        exclude = ('user', 'passed', 'timestamp','passport')