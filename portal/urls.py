from django.urls import path
from .views import apply, SignUp,status

app_name= 'account'


urlpatterns = [
    path('', apply),
    path('signup/', SignUp.as_view(), name='signup'),
    path('status/<int:pk>/',status)
]