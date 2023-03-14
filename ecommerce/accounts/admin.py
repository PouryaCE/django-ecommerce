from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User
from .forms import UserCreationForm, UserChangeForm


# Register your models here.

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ("phone_number", "email", "is_admin")
    list_filter = ('is_admin',)
    search_fields = ('email', "phone_number")
    filter_horizontal = ()
    ordering = ("email",)

    fieldsets = (
        ('اظلاعات کاربر', {'fields': (
            'password', 'phone_number', 'email','first_name', 'last_name', 'age', 'gender', 'bio', 'is_admin',
            'is_active')}),
    )

    add_fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'password1', 'password2')}),
    )


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
