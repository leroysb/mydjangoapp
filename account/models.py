from django.db import models
from django.db.models.deletion import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# create new user and superuser

class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model( email=self.normalize_email(email), )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name=_('email address'), max_length=100, unique=True,)
    username = models.CharField(max_length=14, unique=True)
    full_name = models.CharField(verbose_name=_('full name'), max_length=255, null=True, blank=False)
    date_of_birth = models.DateField(verbose_name=_('date of birth'), null=True)
    # phone_regex = RegexValidator(regex=r'^\+?2547?\d{8}$', message="Phone number must be entered in the format: '+254700000000'.")
    # phone = models.CharField(_('phone number'), validators=[phone_regex], max_length=13, unique=True, null=False, blank=False) # validators should be a list
    headshot = models.ImageField(upload_to='account/headshots', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
        
    def has_module_perms(self, app_label):
        return True