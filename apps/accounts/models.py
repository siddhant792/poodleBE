from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom User Manager class
    """

    def create_user(self, email, password, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        return self.create_user(email, password, True, False)

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        return self.create_user(email, password, True, True)


class User(AbstractBaseUser):
    """
    Custom user class
    """
    email = models.EmailField(unique=True, help_text='Email Address', max_length=50)
    first_name = models.CharField(max_length=50, help_text="First Name of User")
    last_name = models.CharField(max_length=50, help_text="Last Name of User")
    is_staff = models.BooleanField(default=False, help_text="This user can access admin panel")
    is_admin = models.BooleanField(
        default=False, help_text="This user has all permissions without explicitly assigning them"
    )
    password = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their first name and last name
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        # The user is identified by their first name
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
