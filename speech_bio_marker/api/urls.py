from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



app_name = "bio_marker_api" 

urlpatterns = [
    path("", views.home, name="home"),
    path('upload/', views.upload_audio, name='upload_audio'),
    path('search/', views.get_audio, name='get_audio'),
]   


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
