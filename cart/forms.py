from django import forms

#PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 50)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='quantity',max_value = 99 ,min_value = 1,   widget=forms.NumberInput())
    #quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
