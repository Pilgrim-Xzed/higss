from django.urls import path
from .views import apply, SignUp,status, pay, confirm


urlpatterns = [
    path('', apply),
    path('pay/<email>/<pk>', pay, name='pay'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('status/<pk>/',status, name='status'),
    path('confirm/<pk>/', confirm, name='confirm')
]