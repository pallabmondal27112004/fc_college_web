from django.db import models
from baseapp.models import customeruser
import datetime
# Create your models here.
class assignmentlist(models.Model):
    assignment_id=models.ForeignKey(customeruser,on_delete=models.CASCADE,null=True)
    subject_name=models.CharField(max_length=500,null=True)
    deadline=models.DateField(auto_now_add=False)
    date=models.DateField(auto_now=True,null=True,blank=True)
    assignment_file=models.FileField(upload_to='media/',null=True,blank=True )
    def __str__(self):
        return self.subject_name


class assignment(models.Model):
    assignment_id2=models.ForeignKey(customeruser,on_delete=models.CASCADE,null=True)
    subject=models.ForeignKey(assignmentlist,on_delete=models.CASCADE,null=True)
    sent_date=models.DateTimeField(auto_now_add=False,default=datetime.datetime.today(), null=True,blank=True)
    status=models.BooleanField(default=True)
    file=models.FileField(upload_to='media/assignment', null=True,blank=True)

    def __str__(self):
        return self.assignment_id2.first_name +" " + self.assignment_id2.last_name



# studentList=customeruser.objects.filter(catarogy='Student')
class menterList(models.Model):
    mentorName=models.TextField(null=True,blank=True,max_length=200)
    mentorUnderStd=models.ForeignKey(customeruser,on_delete=models.CASCADE)
    qualification=models.TextField(null=True,blank=True,max_length=200)


    def __str__(self):
        return self.mentorName



















































































