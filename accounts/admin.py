from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(DjangoUserAdmin):
    ordering = ('pk',)
    list_display = (
        'email', 'first_name', 'last_name',
        'is_staff', 'is_active')
    # fieldsets = ('Username', {'fields': ('email', 'password')}, 'first_name', 'last_name')


admin.site.register(User, UserAdmin)
