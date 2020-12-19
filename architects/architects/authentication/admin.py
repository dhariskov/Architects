from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from architects.authentication.models import Profile

UserModel = get_user_model()


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profile'


class UserAdmin(UserAdmin):
    inlines = [
        ProfileInlineAdmin,
    ]


admin.site.unregister(UserModel)
admin.site.register(get_user_model(), UserAdmin)
