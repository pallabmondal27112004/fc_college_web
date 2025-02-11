from django import forms
from .models import resumeModel
# GENDER_CHOIES=[
#     ('male', 'male'),
#     ('female', 'female')
# ]
class resumeForm(forms.ModelForm):
    GENDER_CHOIES=[
    ('Male', 'Male'),
    ('Female', 'Female')
]
    LANGUAGE=[
        ('Bengali', 'Bengali'),
        ('English','English'),
        ('Hindi', 'Hindi'),
        ('French','French' )
    ]
    
    gender = forms.ChoiceField(choices=GENDER_CHOIES, widget=forms.RadioSelect)
    languagies = forms.MultipleChoiceField(choices=LANGUAGE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        # gender=forms.ChoiceField(widget=forms.CheckboxSelectMultiple())
        # languagies=forms.ChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'type':'checkbox'}))
        # job_city=forms.MultipleChoiceField(choices=GENDER_CHOIES)
        model=resumeModel
        fields="__all__"
        labels={
        "name":"First Name","dob":"Date of Birth", "gender": "Gender", "pin":"Pin NO.", "Locality": "Address","job_city":"Job Address"
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control chaya', 'placeholder':'Entet name'}),
            'email':forms.TextInput(attrs={'class':'form-control chaya', 'placeholder':'Entet email'}),
            'dob':forms.DateInput(attrs={'class':'form-control chaya ','type':'date','placeholder':'Entet birth of date'}),
            'locality':forms.TextInput(attrs={'class':'form-control chaya','placeholder':'Entet address' }),
            'mobile':forms.NumberInput(attrs={'class':'form-control chaya', 'placeholder':'Enter mobile number'}),
            'my_file':forms.TextInput(attrs={'class':'btn btn-primary', 'placeholder':'input file'}),
            'experience':forms.TextInput(attrs={'class':'form-control chaya' ,'placeholder':'Put you experience'}),
            'hobbies':forms.TextInput(attrs={'class':'form-control chaya', 'placeholder':'Hobbies'}),
            'skill': forms.TextInput(attrs={'class':'form-control chaya', 'placeholder':'Skills'}),
            'objective': forms.Textarea(attrs={'class':'form-control chaya', 'placeholder':'Skills'})
        }
    my_file=forms.FileField(required=False)
    profile_image=forms.ImageField(required=False)
    