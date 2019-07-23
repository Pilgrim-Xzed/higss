from django.urls import path
from .views import apply, SignUp

urlpatterns = [
    path('', apply),
    path('signup/', SignUp.as_view(), name='signup'),
]