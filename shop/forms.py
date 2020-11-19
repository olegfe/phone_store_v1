from shop.models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('plus','minus','comment',)
        
