from django.contrib import admin
from django.urls import path
from . import views
# urls.py
urlpatterns = [
    path("register/",views.registerView.as_view(), name='register'),
    path("",views.loginview.as_view(), name='login'),
    path("logout/",views.logoutViewuser.as_view(), name='logout')
]