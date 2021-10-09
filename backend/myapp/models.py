from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Email address is must')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name


class Profile(models.Model):
    nickname = models.CharField(max_length=20)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='user',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(blank=True, null=True, upload_to='static')

    def __str__(self):
        return self.nickname


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


# 査定金額
class AssesmentPrice(models.Model):
    value = models.IntegerField(blank=True, null=True)
    offer = models.ForeignKey('Offer', related_name='オファー', on_delete=models.PROTECT)
    client_shop = models.ForeignKey('ClientShop', related_name='ショップ', on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.offer} {self.value}円 {self.client_shop}"


class Offer(models.Model):
    item_name = models.CharField(max_length=100)
    item_date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', related_name='カテゴリ', on_delete=models.PROTECT)
    profile = models.ForeignKey('Profile', related_name='プロフィール', on_delete=models.PROTECT)

    def __str__(self):
        return self.item_name


class UserInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    tel = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    # user = models.OneToOneField(User, verbose_name='ユーザー', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class ClientShop(models.Model):
    name = models.CharField(max_length=20)
    kana = models.CharField(max_length=20)
    img = models.ImageField(blank=True, null=True, upload_to='collectstatic')
    manager = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    place = models.CharField(max_length=50)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='client_shop',
        on_delete=models.CASCADE
    )
    assesment_price = models.OneToOneField(
        AssesmentPrice, related_name='assesment_price',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id}　Name:{self.name}"
