from django import forms
from django.core.exceptions import ValidationError


class FormLoginUser(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Email or Mobile',
        'class': 'form-control',

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
          'placeholder':'Enter Your Password',
          'class':'form-control'
    }))

    def clean(self):
        email=self.cleaned_data['email']
        if '@yahoo.com' in email:
            raise ValidationError(
                '%(value)s is include suffix @yahoo.com ',
                params={'value':email},
                code=1
            )



