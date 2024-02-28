from django import forms


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
        max_length=10,
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
              'placeholder': 'متن پیام'
        })
    )

