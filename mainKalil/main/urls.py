from django.urls import path
from . import views
from .views import Register

urlpatterns = [
    # path('', views.index, name='index'),
    path('adminData', views.adminData, name='adminData'),
    path('', Register.as_view(), name='index'),  # окно регистрации
]