from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='گذر واژه', widget=forms.PasswordInput())
    password2 = forms.CharField(label='تایید گذر واژه', widget=forms.PasswordInput())

    class Meta:
        model = User
        exclude = ("password",)

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise ValidationError("کاربری با این شماره تلفن قبلا ثبت شده است")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("کاربری با این ایمیل قبلا ثبت شده است")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password2 and password1 and password1 != password2:
            raise ValidationError("پسورد ها باید یکسان باشند")
        return password2


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you can change password with this <a href=\" ../password \">form</a>")

    class Meta:
        model = User
        fields = "__all__"

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data["phone_number"]
    #     user = User.objects.filter(phone_number=phone_number).exists()
    #     if user:
    #         return ValidationError("کاربری با این شماره تلفن قبلا ثبت شده است")
    #     return phone_number

    # def clean_email(self):
    #     email = self.cleaned_data["email"]
    #     user = User.objects.filter(email=email).exists()
    #     if user:
    #         return ValidationError("کاربری با این ایمیل قبلا ثبت شده است")
    #     return email

    # def clean_password2(self):
    #     password1 = self.cleaned_data["password1"]
    #     password2 = self.cleaned_data["password2"]
    #     if password2 and password1 and password1 != password2:
    #         return ValidationError("پسورد ها باید یکسان باشند")
    #     return password2
