import re
import _md5
from django.core.exceptions import ObjectDoesNotExist

from django import forms

from WebbChat.models import User


def hashlib_md5(msg):
    password_md5 = _md5.md5(msg.encode("utf-8")).hexdigest()
    return password_md5


class FormLogin(forms.Form):
    """init form login"""
    name = forms.CharField(label='name', max_length=100)
    password = forms.CharField(label='password', max_length=100)


class FormRegister(forms.Form):
    """
       Describe: init form Register
    """
    name = forms.CharField(label='name', max_length=250)
    email = forms.CharField(label='email', max_length=250)
    password = forms.CharField(label='password', max_length=250)
    course = forms.CharField(label='course', max_length=250)
    gifted = forms.CharField(label='gifted', max_length=250)
    hobby = forms.CharField(label='hobby', max_length=200)
    desire = forms.CharField(label='desire', max_length=200)

    def clean_user(self):
        name = self.cleaned_data['name']
        if not re.search(r'^\w+$', name):
            raise forms.ValidationError('ten tai khoan co ki tu dac biet')
        try:
            User.objects.get(name=name)
        except ObjectDoesNotExist:
            return name
        raise forms.ValidationError('tai khoan da ton tai')

    def hashlib_md5(self):
        password = self.cleaned_data['password']
        password_md5 = _md5.md5(password.encode('utf-8')).hexdigest()
        return password_md5

    def save_user(self):
        """
        Describe: dang ki mot user moi
        :return: not return
        """
        User.objects.create(name=self.clean_user(),
                            email=self.cleaned_data['email'],
                            password=self.hashlib_md5(),
                            course=self.cleaned_data['course'],
                            gifted=self.cleaned_data['gifted'],
                            hobby=self.cleaned_data['hobby'],
                            desire=self.cleaned_data['desire'],
                            )
