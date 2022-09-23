from django import forms
from mainapp.models import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', ]



    