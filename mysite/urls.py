from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from mysite.core import views


# router=routers.DefaultRouter()
# router.register('api/upload', views.upload,'upload')
urlpatterns = [
    #path('', views.upload, name='upload'),
    path('api/upload/', views.upload, name='upload'),
    # path('api/download/', views.download_file, name='upload'),
    path('admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

