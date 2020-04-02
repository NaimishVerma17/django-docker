from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from app.core import models


# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'name']
    ordering = ['id']
    fieldsets = (
        (
            None,
            {'fields': ('email', 'name')}
        ),
        (
            _('Personal Info'),
            {'fields': ('name',)}
        ),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (
            _('Important dates'),
            {'fields': ('last_login',)}
        )
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        )
    )


admin.site.register(models.User, UserAdmin)
