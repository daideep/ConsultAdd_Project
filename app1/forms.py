from django import forms
from django.core import validators


def check_password(password):
    #password = self.cleaned_data['password']
    if len(password) > 5:
        raise forms.ValidationError("Password length should be less than 5")



class Registerform(forms.Form):
    name = forms.CharField(max_length=30, label="Name")
    email = forms.EmailField(max_length=30, label="Email")
    confirm_email = forms.EmailField(max_length=30, label='Confirm Email')
    text = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput, validators=[check_password])

    def Valid_Email(self):
        email = self.cleaned_data['email']
        confirm_email = self.cleaned_data['confirm_email']
        if email != confirm_email:
            raise forms.ValidationError("Email doesn't match")