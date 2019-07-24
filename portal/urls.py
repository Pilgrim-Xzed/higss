from django.urls import path
from .views import apply, SignUp,status, pay


urlpatterns = [
    path('', apply),
    path('pay/<email>/  ', pay, name='pay'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('status/<int:pk>/',status)
]