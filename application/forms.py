from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Student_table

class Student_form(forms.ModelForm):
    class Meta:
        model = Student_table
        fields = ['name','email','contact','course','city','password']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Full Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email-Id'}),
            'contact':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mobile no.'}),
            'course':forms.TextInput(attrs={'class':'form-control','placeholder':'Course Name'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City Name'}),
            'password':forms.PasswordInput(render_value=True ,attrs={'class':'form-control','placeholder':'Enter Password'}),
        }