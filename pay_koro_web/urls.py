from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.Registration_api, name='registration')
]

