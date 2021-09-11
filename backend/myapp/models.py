from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Offer(models.Model):
    item_name = models.CharField(max_length=100)
    item_date = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, related_name='offers', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
