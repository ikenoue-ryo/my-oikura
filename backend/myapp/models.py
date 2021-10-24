from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.core.validators import RegexValidator
from django.utils import timezone


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
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号') 

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
    grade = models.CharField(max_length=30, blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
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
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号') 
    prefectures = models.CharField(max_length=20)
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


class ClientMessage(models.Model):

    message = models.CharField(max_length=500)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='sender',
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='receiver',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


# class Brand(models.Model):

#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


class Car(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name


SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]


class ShopReview(models.Model):
    client_shop = models.ForeignKey('ClientShop', on_delete=models.PROTECT)
    comment = models.CharField(max_length=100)
    score = models.PositiveSmallIntegerField(verbose_name='レビュースコア', choices=SCORE_CHOICES, default='3')
    profile = models.ForeignKey('Profile', related_name='profile', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    
    def get_percent(self):
        percent = round(self.score / 5 * 100)
        return percent


# 来店予約
class VisitReservation(models.Model):
    start = models.DateTimeField('開始時間')
    name = models.CharField('予約者名', max_length=30)
    tel = models.CharField('電話番号', max_length=30)
    email = models.CharField('Email', max_length=30)
    comment = models.CharField('コメント', max_length=500)
    reservation_shop = models.ForeignKey('ClientShop', related_name='予約店舗', on_delete=models.PROTECT)

    def __str__(self):
        start = timezone.localtime(self.start).strftime('%Y/%m/%d %H:%M:%S')
        return f'{self.name} {start} ~'


# 店舗PR
class ClientPr(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='client_author',
        on_delete=models.CASCADE
    )
    client_shop = models.ForeignKey('ClientShop', related_name='client_shop', on_delete=models.PROTECT)
    text = models.CharField('ブログ', max_length=500)
    img = models.ImageField(blank=True, null=True, upload_to='static')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.text
