from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Application
from .forms import ApplicationForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def apply(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.user = request.user
            model_instance.save()
            return redirect('/status/', {'result_data':model_instance })
 
    else:
 
        form = ApplicationForm()
        return render(request, 'home.html', {'form': form})

def status(request):
    # Return all applications for case of multiple
    return render(request, 'status.html', {'result_data':request})