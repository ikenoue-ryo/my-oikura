from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from myapp.models import User, Offer, Category, Profile, ClientShop, AssesmentPrice,ClientMessage, Car


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientShop)
class ClientShopAdmin(admin.ModelAdmin):
    pass


@admin.register(AssesmentPrice)
class AssesmentPriceAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientMessage)
class ClientMessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
