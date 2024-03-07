from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import  EmailValidator, MaxLengthValidator


class UserForms(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            MaxLengthValidator(100),
            EmailValidator
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور با هم یکسان نیست')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            MaxLengthValidator(100),
            EmailValidator
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput
    )