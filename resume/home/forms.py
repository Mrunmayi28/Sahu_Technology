from django.core import validators
from django import forms
from django.db.models import fields
from .models import details

class add_details(forms.ModelForm):
    class Meta:
        model = details
        fields = ['Fname','Lname','Email','Number','Dname','Branch','Dscore','Styear','Dyear','Hsc','Hscore','Hyear','Ssc','Sscore','Syear','Experience','Skills','Awards']
        widgets = {
            'Fname':forms.TextInput(attrs={'class':'form-control'}),
            'Lname':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.TextInput(attrs={'class':'form-control'}),
            'Number':forms.TextInput(attrs={'class':'form-control'}),
            'Dname':forms.TextInput(attrs={'class':'form-control'}),
            'Branch':forms.TextInput(attrs={'class':'form-control'}),
            'Dscore':forms.TextInput(attrs={'class':'form-control'}),
            'Styear':forms.TextInput(attrs={'class':'form-control'}),
            'Dyear':forms.TextInput(attrs={'class':'form-control'}),
            'Hsc':forms.TextInput(attrs={'class':'form-control'}),
            'Hscore':forms.TextInput(attrs={'class':'form-control'}),
            'Hyear':forms.TextInput(attrs={'class':'form-control'}),
            'Ssc':forms.TextInput(attrs={'class':'form-control'}),
            'Sscore':forms.TextInput(attrs={'class':'form-control'}),
            'Syear':forms.TextInput(attrs={'class':'form-control'}),
            'Experience':forms.TextInput(attrs={'class':'form-control'}),
            'Skills':forms.TextInput(attrs={'class':'form-control'}),
            'Awards':forms.TextInput(attrs={'class':'form-control'})
        }