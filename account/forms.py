from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser,AdressUser


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


class RegisterUserForm(forms.ModelForm):

    ConfirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'ConfirmPassword',
        'class': 'form-control'
    }))

    class Meta:
        choise = [
            ('1', 'زن'),
            ('0', 'مرد')
        ]

        model=CustomUser
        fields=('Firstname','Lastname','NationalCode','password','ConfirmPassword','Mobile','Address','email','Gender')
        widgets={

            'Firstname': forms.TextInput(attrs={
                'placeholder': 'Firstname',
                'class': 'form-control',
            }),

            'Lastname':forms.TextInput(attrs={
               'placeholder':'Lastname',
               'class':'form-control'
              }),
            'NationalCode':forms.TextInput(attrs={
               'placeholder':'NationalCode',
               'class':'form-control'

              }),
            'Mobile':forms.TextInput(attrs={
               'placeholder':'Mobile',
               'class':'form-control'
              }),
            'Address':forms.TextInput(attrs={
               'placeholder':'Address',
               'class':'form-control'
              }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control',

            }),

            'email':forms.TextInput(attrs={
               'placeholder':'email',
               'class':'form-control'
              }),
            'Gender':forms.Select(choices=choise,attrs={
                 'class':'form-control col-2'
            })
        }

    def clean(self):
        password=self.cleaned_data['password']
        ConfirmPassword=self.cleaned_data['ConfirmPassword']
        if password!=ConfirmPassword:
            raise ValidationError(
                'Password and ConfirmPassword not match',
                  code=2
            )

    def __init__(self,*args,**kwargs):
        super(RegisterUserForm, self).__init__(*args,**kwargs)
        self.fields['Firstname'].required=False


class ForgetPasswordUser(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('Mobile',)
        widgets={
               'Mobile':forms.TextInput(attrs={
                   'placeholder':'Mobile',
                   'class':'form-control col-7'
              }),
        }


class AdressForm(forms.ModelForm):
    class Meta:
        model=AdressUser
        exclude=('userid',)
        widgets={
            'title':forms.TextInput(attrs={
                'class':'form-control form-group',
                'placeholder':'Adress',
                'size':60
            }),

            'ZipCode':forms.TextInput(attrs={
                'class': 'form-control form-group',
                'placeholder':'ZipCode'
            }),
            'mobile':forms.TextInput(attrs={
                'class':'form-control form-group',
                'placeholder':'mobile'
            })
        }

