from django import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static

from Project import settings

urlpatterns = [
                  path('admin/', admin.site.urls),  # open
                  path('', TemplateView.as_view(template_name='main/adminData.html'), name='adminData'),
                  path('users/', include('users.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
