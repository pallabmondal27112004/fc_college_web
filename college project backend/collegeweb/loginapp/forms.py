from django import forms
from .models import customeruser
from django.contrib.auth.models import User

class userform(forms.ModelForm):
    class Meta:

        model = customeruser  
        fields = ['first_name', 'last_name','email','catagory','phone', 'image','password']  # List of fields to include in the form
        labels={
            'first_name':"first_name", 'last_name':"last_name",'email':"email",'password':"password",'phone':"phone"

        }
        widgets = {
            'email': forms.EmailInput(attrs={'id':'inputset',' class': ' me-3 w-100 md-form-control', }),
            'first_name': forms.TextInput(attrs={'id':'inputset',' class': ' me-3 md-form-control',}),
            'last_name': forms.TextInput(attrs={'id':'inputset',' class': ' me-3 md-form-control',}),
            # 'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.TextInput(attrs={'id':'inputset',' class': ' me-3  md-form-control', 'required':False}),
            'phone': forms.TextInput(attrs={'id':'inputset',' class': ' me-3 md-form-control', 'placeholder': 'phone'}),
            'catagory': forms.RadioSelect(attrs={'class': 'ps-2 fs-6 ',}),
        }
  