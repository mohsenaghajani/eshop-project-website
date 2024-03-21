from django import forms
from django.core.exceptions import ValidationError

from account.models import User


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar_image', 'address', 'about_user']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'avatar_image': forms.FileInput(attrs={
                'class': 'form-control',

            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'message'
            }),
            'about_user': forms.TextInput(attrs={
                'class': 'form-control',
                'row': 8
            }),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar_image': 'عکس پروفایل',
            'address': 'آدرس',
            'about_user': 'درباره من'
        }


class ChangePassForm(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور با هم یکسان نیست')
