from .models import User
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, password):
        if not phone_number:
            raise ValueError("کاربر باید حتما شماره تلفنی داشته باشد")
        if not email:
            raise ValueError("کاربر باید حتما ایمیلی داشته باشد")
        if not password:
            raise ValueError("کاربر باید حتما پسوردی داشته باشد")
        user = self.model(phone_number=phone_number, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, first_name, last_name, password):
        user = self.create_user(phone_number, email, password)
        user.is_admin = True
        user.first_name = first_name
        user.last_name = last_name
        user.save(using=self._db)
