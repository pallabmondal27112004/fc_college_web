from django.db import models
from django.contrib.auth.models import AbstractUser
from . import manager
import PIL
class catagory(models. Model):
    name=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name
class customeruser(AbstractUser):

    # CHOICE=(
    #     ('Hod','Hod'),
    #     ('Teacher','Teacher'),
    #     ('Staff','Staff'),
    #     ('Student','Student')
    # )
    username=None
    email=models.EmailField(unique=True, null=True)
    phone=models.CharField(max_length=13, null=True)
    catagory=models.ForeignKey(catagory,on_delete=models.CASCADE,null=True)
    is_superuser=models.BooleanField(default=True)
    image=models.ImageField(upload_to='media/',null=True,blank=True)
    objects=manager.usermanager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['password']
