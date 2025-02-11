from django.urls import path
from . import views
urlpatterns=[
    path("home/",views.dashboardIndex.as_view(), name='dashboard'),
    path("student/details/",views.showStudent.as_view(), name='studentDetails'),
    path("student/delete/<int:pk>/",views.deleteStudent.as_view(), name='deleteStudent'),
    path("student/edit/<int:pk>/",views.editStudent.as_view(), name='editStudent'),
    path("cource/details/",views.showCource.as_view(), name='courceDetails'),
    path("cource/delete/<int:pk>/",views.deleteCource.as_view(), name='deleteCource'),
    path("cource/edit/<int:pk>/",views.editCource.as_view(), name='editCource'),
    path("assignment/",views.assignmentView.as_view(), name='assignment'),
    # path("editprofile/<int:pk>",views.editprofile.as_view(), name='editprofile'),

]