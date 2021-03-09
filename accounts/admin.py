from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser
# Register your models here.
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'password', 'genre', 'roles', 'about', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('genre', 'roles', 'about',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('genre', 'roles', 'about',)}),
    )

admin.site.register(CustomUser, UserAdmin)