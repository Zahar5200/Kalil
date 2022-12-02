from django.urls import path
from . import views
from .views import Register

urlpatterns = [
    path('', views.index, name='index'),
    path('adminData', views.adminData, name='adminData'),
    path('register/', Register.as_view(), name='register')
]