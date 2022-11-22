# from django import forms
from django import forms
from .models import TextModel

class ApiForm(forms.ModelForm):
    
    class Meta:
        model = TextModel
        fields = "__all__"
        labels = {
            'slug' : 'Entrez votre crypto ici',
			'convert' : 'Entrez votre devise ici'
        }