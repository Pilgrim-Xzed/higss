from django.urls import path
from .views import apply, SignUp,status

urlpatterns = [
    path('', apply),
    path('signup/', SignUp.as_view(), name='signup'),
    path('status/',status)
]