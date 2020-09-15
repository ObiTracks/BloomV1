from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, apt, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not first_name:
            raise ValueError("User must enter a first name")
        if not last_name:
            raise ValueError("User must enter a last name")
        if not apt:
            raise ValueError("User must have an apartment number")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            apt = apt,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, apt, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            apt = apt,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(verbose_name="first name", max_length=30)
    last_name = models.CharField(verbose_name="last name", max_length=30)
    email = models.EmailField(verbose_name="email", max_length=80, unique=True)
    apt = models.IntegerField(verbose_name="apartment number")
    
    # Required fields for creating a custom user model
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','apt']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True