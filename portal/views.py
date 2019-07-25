from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Application
from .forms import ApplicationForm, CheckForm
from django.http import HttpResponse

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def apply(request):
    applications = Application.objects.all()
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            url = '/status/{}/'.format(model_instance.id)
            return redirect(url, {'result_data':model_instance })
 
    else:
 
        form = ApplicationForm()
    return render(request, 'home.html', {'form': form, 'applications': applications})

def status(request, pk):
    application = Application.objects.get(id=pk)
    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponse("Yessss!!")
 
    else:
 
        form = ApplicationForm(instance=application)
    return render(request, 'status.html', {'form': form, 'pk': pk})

def pay(request, email, pk):
    redirect_url = '/confirm/'
    return render(request, 'pay.html', {'email': email, 'redirect_url': redirect_url})

def success(request):
    return render(request, 'success.html', {})

def pay_fee(request, pk, email, fee):
    amount = int(fee) * 100 
    redirect_url = '/success/'
    return render(request, 'pay_fees.html', {'email': email, 'redirect_url': redirect_url, 'amount': amount})

def confirm(request):
    application = None
    if request.method == "POST":
        form = CheckForm(request.POST)
        if form.is_valid():
            try:
                application=Application.objects.get(admission_number=form.cleaned_data['admission_number'])
            except Application.DoesNotExist:
                application = None
            print(application)

    else:
        form = CheckForm()
    return render(request, 'confirm.html', {'form': form, 'application': application})