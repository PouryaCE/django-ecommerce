from django import forms
from django.core.exceptions import ValidationError

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='گذر واژه', widget=forms.PasswordInput())
    password2 = forms.CharField(label='تایید گذر واژه', widget=forms.PasswordInput())

    class Meta:
        model = User
        exclude = ("password",)

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if User.objects.get(phone_number=phone_number).exists():
            return ValidationError("کاربری با این شماره تلفن قبلا ثبت شده است")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.get(email=email).exists():
            return ValidationError("کاربری با این ایمیل قبلا ثبت شده است")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password2 and password1 and password1 != password2:
            return ValidationError("پسورد ها باید یکسان باشند")
        return password2


