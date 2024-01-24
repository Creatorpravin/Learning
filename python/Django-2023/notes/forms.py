from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('tittle', 'text')
        widgets = {
            'tittle': forms.TextInput(attrs={'class' : 'form-control my-5'}),
            'text' : forms.Textarea(attrs={"class": "form-control mb-5"})
        }
        labels = { 
            'text' : "Write your thoughts here:"}

    def clean_tittle(self):
        tittle = self.cleaned_data['tittle']
        if 'Django' not in tittle:
            raise ValidationError('we only accept notes about Django!')
        return tittle
