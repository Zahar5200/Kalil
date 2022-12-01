from django.urls import path, include

from Project import settings
from .views import Register
from django.conf.urls.static import static

urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # система аутентификация API
    path('register/', Register.as_view(), name='index'),  # окно регистрации
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
