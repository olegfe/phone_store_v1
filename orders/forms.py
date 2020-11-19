from django import forms
from .models import Order
from django.contrib.auth.models import User


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [ 'email',  'postal_code', 'city', 'street',]
        widgets = {
            'email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "e-mail"}),
            'postal_code': forms.TextInput(attrs={"class": "form-control", "placeholder": "Почтовый индекс"}),
            'city': forms.TextInput(attrs={"class": "form-control", "placeholder": "Город"}),
            'street': forms.TextInput(attrs={"class": "form-control", "placeholder": "Улица"}),
 
            }

  
