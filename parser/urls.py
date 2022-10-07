from parser import views

from django.urls import include, path, re_path
from rest_framework import routers

urlpatterns = [
    path('upload/', views.UploadViewSet.as_view(), name='base-text-file-parser-url')
]
