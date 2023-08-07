from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories']

        
# class LoginForm(forms.ModelForm):
#         fields = ['ussername', 'password']

