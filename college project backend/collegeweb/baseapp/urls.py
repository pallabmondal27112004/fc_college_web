from django.contrib import admin
from django.urls import path

from  . import views
urlpatterns = [
    path("student/",views.studentsayView.as_view(), name='studentsay'),
    path("cource/",views.courceView.as_view(), name='cource'),
    path("testimonial/",views.testimonialView.as_view(), name='testimonial'),
    path("about/",views.aboutview.as_view(), name='about'),
    path("courcedetails/",views.courceDetailsView.as_view(), name='courcedetails'),

    # path("/feature/",projectview, name='feature'),

    path("home/",views.indexView.as_view(), name='home'),
    path("contect/",views.contectView.as_view(), name='contect'),
    

]  