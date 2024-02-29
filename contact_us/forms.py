from django import forms

from contact_us.models import ContactUs


class ContactUsForms(forms.Form):
    subject = forms.CharField(
        max_length=30,
        label='عنوان',
        error_messages={
            'required': 'لطفا عنوان را وارد کنید',
            'max_length': 'تعداد کارکتر ها باید کمتر از 300 باشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'عنوان',
        })
    )

    email = forms.EmailField(
        max_length=300,
        label='ایمیل',
        error_messages={
            'required': 'لطفا ایمیل را وارد کنید',
            'max_length': 'تعداد کارکتر ها باید کمتر از 300 باشد'
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل',
        })
    )
    full_name = forms.CharField(
        max_length=30,
        label='نام و نام خانوادگی',
        error_messages={
            'required': 'لطفا نام و نام خانوادکی را وارد کنید',
            'max_length': 'تعداد کارکتر ها باید کمتر از 300 باشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی',

        })
    )
    message = forms.CharField(
        label='متن پیام ',
        widget=forms.Textarea(attrs={
              'class':'form-control',
              'placeholder': 'متن پیام',
              'id': 'message'
        })
    )


class ContactUsModelForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان',
            }),
            'message': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'متن پیام',
                'id': 'message'
            }),
        }
        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی را وارد کنید'
            }
        }


