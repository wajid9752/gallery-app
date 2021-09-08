
from django.urls import path
from .views import *



urlpatterns = [
    path('',         home ,         name="home"),
    path('upload/',  upload_file,   name="upload")  
]