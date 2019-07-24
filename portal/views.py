from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Application
from .forms import ApplicationForm
from django.http import HttpResponse

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
            url = '/status/{}/'.format(model_instance.id)
            return redirect(url, {'result_data':model_instance })
 
    else:
 
        form = ApplicationForm()
    return render(request, 'home.html', {'form': form})

def status(request, pk):
    application = Application.objects.get(id=pk)
    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.user = request.user
            model_instance.save()
            return HttpResponse("Yessss!!")
 
    else:
 
        form = ApplicationForm(instance=application)
    return render(request, 'status.html', {'form': form, 'pk': pk})

def pay(request, email, pk):
    redirect_url = '/confirm/{}/'.format(pk)
    return render(request, 'pay.html', {'email': email, 'redirect_url': redirect_url})

def confirm(request, pk):
    pk = int(pk)
    application = Application.objects.get(id=pk)
    return render(request, 'confirm.html', {'pk': pk, 'application': application})