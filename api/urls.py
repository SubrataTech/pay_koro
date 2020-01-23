from api.registration import Register
from django.urls import path, include
from . import views

urlpatterns = [
    # Registration Api
    path('register/', Register.as_view({'post': 'create'}), name='register')
]
