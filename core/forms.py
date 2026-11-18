from django import forms
from .models import ItemOrRecord

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemOrRecord
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }