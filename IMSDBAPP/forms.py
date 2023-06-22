from django import forms
from .models import AddPurchase

class AddPurchaseForm(forms.ModelForm):
    class Meta:
        model = AddPurchase
        fields = '__all__'
