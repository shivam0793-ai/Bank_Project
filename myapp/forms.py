from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import CreateAccount
from django.core.validators import *

class signup_form(UserCreationForm):

    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))

    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Email Address"
        })
    )


    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm Password"
        })
    )

    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.help_text=""




class create_account_form(forms.ModelForm):
    class Meta:
        model=CreateAccount
        exclude=['user']


from django import forms
from django.core.validators import RegexValidator


class money_transfer_form(forms.Form):

    sender = forms.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\d{12}$',
                message='Account number must be exactly 12 digits.'
            )
        ]
    )

    receiver = forms.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\d{12}$',
                message='Account number must be exactly 12 digits.'
            )
        ]
    )

    amount = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        min_value=1
    )