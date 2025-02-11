from django.db import models
from PIL import Image
from loginapp.models import customeruser



# Create your models here.

class students(models.Model):
    # student_id=models.ForeignKey(customeruser,on_delete=models.CASCADE, null=True)
    student_id=models.ForeignKey(customeruser,null=True,on_delete=models.CASCADE)
    name=models.TextField(max_length=20)
    job=models.TextField(max_length=200)
    image=models.ImageField(upload_to="media/", null=True, blank=True )

    def __str__(self):
        return self.name

#cource models
class cources(models.Model):
    cource_id=models.ForeignKey(customeruser,null=True,on_delete=models.CASCADE)
    courceName=models.TextField(max_length=200)
    host=models.TextField(max_length=200)
    rating=models.TextField(max_length=110)
    image=models.ImageField(upload_to="media/", null=True, blank=True )


    def __str__(self):
        return self.courceName
    
# models
class testimonial(models.Model):
    say=models.TextField(max_length=2000)
    Sname=models.TextField(max_length=200)
    role=models.TextField(max_length=110)
    image=models.ImageField(upload_to="media/", null=True, blank=True )


    def __str__(self):
        return self.Sname