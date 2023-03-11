from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager


# Create your models here.


class User(AbstractBaseUser):
    gender_choices = (
        ('f', 'female'),
        ('m', 'male')
    )
    phone_number = models.CharField(max_length=11, verbose_name='شماره همراه')
    email = models.EmailField(verbose_name='ایمیل')
    first_name = models.CharField(max_length=30, verbose_name='نام', null=True, blank=True)
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی', null=True, blank=True)
    age = models.SmallIntegerField(verbose_name='سن', null=True, blank=True)
    gender = models.CharField(max_length=30, choices=gender_choices, verbose_name='جنسیت', default='m')
    bio = models.TextField(verbose_name='بیو گرافی', null=True, blank=True)
    is_admin = models.BooleanField(default=False, verbose_name='آیا کاربر ادمین است؟')
    is_active = models.BooleanField(default=True, verbose_name='آیا کاربر فعال است؟')

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    # methods
    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.phone_number}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
