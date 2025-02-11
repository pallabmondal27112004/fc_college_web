from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class resumeModel(models.Model):
    GENDER_CHOIES=[
    ('Male', 'Male'),
    ('Female', 'Female')
]
    STATE_CHOISE=[
        ('Maharashtra', 'Maharashtra'), 
        ('Karnataka', 'Karnataka'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Kerala', 'Kerala'),
        ('Gujarat', 'Gujarat'),
        ('Rajasthan', 'Rajasthan'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('West Bengal', 'West Bengal'),
        ('Punjab', 'Punjab'),
        ('Bihar', 'Bihar')
    ]
    EXPERIENCE=[
        ( True, 'YES'),
        (False, 'NO')
    ]
  
    name=models.CharField(max_length=50,null=True)
    objective=models.CharField(max_length=200, null=True)
    email= models.EmailField()
    dob = models.DateField()
    gender= models.CharField(max_length=10, choices=GENDER_CHOIES)
    skill  =models.CharField(max_length=50, null=True)
    locality=models.CharField(max_length=100)
    # city= models.CharField(max_length=100)
    # pin= models.IntegerField()
    # state=models.CharField(max_length=100, choices=STATE_CHOISE)
    mobile= models.IntegerField()
    hobbies=models.CharField(max_length=50, null=True)
    languagies=models.CharField(max_length=50, null=True)
    experience= models.CharField(max_length=100)
    profile_image= models.ImageField(upload_to="profile/image/", blank=True, null=True)
    my_file=models.FileField(upload_to="profile/file/", blank=True, null=True)

    def __str__(self):
        return self.name
    



