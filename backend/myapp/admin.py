from django.contrib import admin
from .models import User, Offer, Category


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'password')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'item_date', 'created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
