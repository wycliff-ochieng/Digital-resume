from django import forms
from .models import ContactProfile

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    widget = forms.TextInput(attrs={
        'placeholder':'Ful Name',
    })
    email = forms.EmailField(max_length=100,required=True)
    widget = forms.TextInput(attrs={
        'placeholder':'Email',
    })
    message = forms.TimeField(required=True)
    widget = forms.Textarea(attrs={
        'placeholder':'Message',
        'rows':'6'
    })

    class Meta:
        model = ContactProfile
        fields = ['name','email','message']