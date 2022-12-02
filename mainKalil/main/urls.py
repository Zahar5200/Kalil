from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminData', views.adminData, name='adminData'),
]