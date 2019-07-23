from django.urls import path
from .views import apply, SignUp,status, pay

app_name= 'account'


urlpatterns = [
    path('', apply),
    path('pay/', pay),
    path('signup/', SignUp.as_view(), name='signup'),
    path('status/<int:pk>/',status)
]