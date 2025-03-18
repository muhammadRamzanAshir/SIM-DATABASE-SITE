from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('get_mobile_details/', views.get_mobile_details, name='get_mobile_details'),
    path('save_phone_detail/', views.save_phone_detail, name='save_phone_detail'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)