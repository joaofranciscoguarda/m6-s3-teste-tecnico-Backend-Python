from parser import views

from django.urls import include, path, re_path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'upload', views.UploadViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls), name='base-text-file-parser-url')
]
