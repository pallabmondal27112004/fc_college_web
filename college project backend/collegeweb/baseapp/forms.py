from django import forms
from .models import students,cources,testimonial

# student form 
class studentForm(forms.ModelForm):
    
    class Meta:
        model= students
        fields='__all__'
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}),
            'job':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your job role'}),
            'iamge': forms.FileInput(attrs={'class':'form-control'}),
            'student_id': forms.TextInput(attrs={'class':'d-none'})
        }
    image=forms.FileField(required=False)

# cource form 
class courceForm(forms.ModelForm):
    
    class Meta:
        model= cources
        fields="__all__"
        widgets={
            "courceName":forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your cource name'}),
            'host':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your host name'}),
            'iamge': forms.FileInput(attrs={'class':'form-control'}),
            'rating':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter rating'}),
        }
    image=forms.ImageField(required=False)

class testiForm(forms.ModelForm):
    
    class Meta:
        model= testimonial
        fields="__all__"
        widgets={
            "say":forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your openion', 'type':'textarea','style':'max-height: 150px;'}),
            'Sname':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your name'}),
            'role':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter job role'}),
            'iamge': forms.FileInput(attrs={'class':'form-control'}),
        }
    image=forms.ImageField(required=False)