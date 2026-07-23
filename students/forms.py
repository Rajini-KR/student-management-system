from django import forms
from django.contrib.auth import get_user_model
from .models import Student

User= get_user_model()
class StudentForm(forms.ModelForm):

    user=forms.ModelChoiceField(
        queryset=User.objects.filter(role="STUDENT"),
        empty_label="Select Student User"
    )
    class Meta:
        model=Student

        fields=[
            'user',
            'dob',
            'gender',
            'cgpa',
            'photo',
            'department',
            'courses',
        ]
        widgets={
            'dob':forms.DateInput(attrs={'type':'data'}),
            'courses':forms.CheckboxSelectMultiple()
        }

        
        def clean_cgpa(self):
            cgpa=self.cleaned_data['cgpa']
            if cgpa <0 or cgpa >10:
                raise forms.ValidationError("CGPA musdt be between 0 and 10,")
            return cgpa