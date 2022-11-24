from django import forms

class UserRgistrationForm(forms.Form):
    nombre=forms.CharField()