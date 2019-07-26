from django.urls import path
from .views import apply, SignUp,status, pay, pay_fee, confirm, success


urlpatterns = [
    path('admissions/', apply),
    path('pay/<email>/<pk>', pay, name='pay'),
    path('pay_fee/<email>/<pk>/<fee>', pay_fee, name='pay_fee'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('status/<pk>/',status, name='status'),
    path('fees/', confirm, name='confirm'),
    path('success/', success),
]