from django import forms
from account.models import User


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar_image', 'address']
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
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar_image': 'عکس پروفایل',
            'address': 'آدرس',
        }

