from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import home, about, faq
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('property/', include('property.urls', namespace='property')),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),


    path('admin/', admin.site.urls)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
