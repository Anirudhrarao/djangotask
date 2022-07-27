from dataclasses import field
from django import forms 
from .models import User, DoctoBlog
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class DoctorForm(UserCreationForm):
    class Meta():
        model = User 
        fields = ['first_name','last_name','username','email','profile','is_doctor','address','city','state','pincode']

class PatientForm(UserCreationForm):
    class Meta():
        model = User 
        fields = ['first_name','last_name','username','email','profile','is_patients','address','city','state','pincode']

class DoctorLogin(AuthenticationForm):
    class Meta():
        model = User 
        fields = ['username','password']

class PatientLogin(AuthenticationForm):
    class Meta():
        model = User 
        fields = ['username','password']

class BlogFormCreations(forms.ModelForm):
    class Meta():
        model = DoctoBlog
        fields = ['title','image','category','summary','content','status']