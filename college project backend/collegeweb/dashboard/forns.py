from django import forms
from .models import assignment, assignmentlist
class doAssignmentForm(forms.ModelForm):
    class Meta:
        model= assignment
        fields=['assignment_id2','subject', 'status','file','sent_date']
        widgets={
            # 'deadline':forms.DateTime0Inputattrs={'type': 'data','placeholder': "fdgjdfhgu"}()
            
        }