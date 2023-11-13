from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserModel
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['company_name', 'username']
    fieldsets = (
        (None, {'fields': ('company_name', 'username', 'password')}),
        (
            _('permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('important dates'), {'fields': ('last_login', )}),
    )
    
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('company_name', 'username', 'password1', 'password2'),
            },
        ),
    )

admin.site.register(UserModel, UserAdmin)
