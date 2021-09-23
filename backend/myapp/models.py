from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    password = models.CharField(max_length=50, db_index=True)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Offer(models.Model):
    item_name = models.CharField(max_length=100)
    item_date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    # author = models.ForeignKey(User, related_name='offers', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name


class UserInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    tel = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)

    def __str__(self):
        return self.name
