from django.contrib.auth.models import BaseUserManager
class CustomerUserManager(BaseUserManager):
    def create_user(self,email,password,phone,name,**extra_fields):
        if not email:
            raise ValueError("email is required for every user!")
        email=self.normalize_email(email)
        user=self.model(email=email,phone=phone,name=name,**extra_fields)

        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,phone,name,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('super user must have staff user!')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True!')
        return self.create_user(email,password,phone,name,**extra_fields)