from django import forms
from django.forms import ModelForm
from myapp.models import *

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = '__all__'
        labels = {
            'title' : 'titulo',
            'description': 'descricao',
            'image': 'imagem',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Camisa'
                }
            ),
            'descripion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Camisa de Algodão'
                }
            ),
            'image': forms.ClearableFileInput(),
        }