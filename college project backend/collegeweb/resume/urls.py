from django.contrib import admin
from django.urls import path
from .views import resumeUploder,cvView
urlpatterns = [
   
    path("",resumeUploder, name="resumeUploder1"),
    path("<int:pk>/",cvView, name="cvView")
]
