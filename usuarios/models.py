from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UsuarioManager(BaseUserManager):
    def create_user(
            self, email, country, city, comuna, address, cellphone,
            birthdate, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UsuarioManager.normalize_email(email),
            country=country, city=city, comuna=comuna, address=address,
            cellphone=cellphone, birthdate=birthdate,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, email, country, city, comuna, address, cellphone,
            birthdate, password):
        user = self.create_user(
            email,
            password=password,
            country=country, city=city, comuna=comuna, address=address,
            cellphone=cellphone, birthdate=birthdate,)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    #username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True)
    comuna = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    cellphone = models.IntegerField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='pictures', blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    coordinates = models.CharField(max_length=255, blank=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [
        'country', 'city', 'comuna', 'address', 'cellphone', 'birthdate']

    def get_full_name(self):
        # For this case we return email. Could also be User.first_name
        # User.last_name if you have these fields
        return self.email

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you
        # have this field
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
