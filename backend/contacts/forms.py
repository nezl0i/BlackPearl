from django.forms import ModelForm, TextInput, EmailInput
from django.forms import Textarea
from .models import Contact


class ContactForm(ModelForm):

    class Meta:

        model = Contact
        fields = ['username', 'email', 'phone', 'message']
        widgets = {
            'username': TextInput(
                attrs={
                    "placeholder": "Имя",
                    "class": "form-control footer-input margin-b-20"
                }
            ),
            'email': EmailInput(
                attrs={
                    "placeholder": "Email",
                    "class": "form-control footer-input margin-b-20"
                }
            ),
            'phone': TextInput(
                attrs={
                    "placeholder": "Телефон",
                    "class": "form-control footer-input margin-b-20"
                }
            ),
            'message': Textarea(
                attrs={
                    'placeholder': 'Сообщение',
                    "class": "form-control footer-input margin-b-30"
                }
            ),
        }
