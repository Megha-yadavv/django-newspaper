from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .form import CustomChangeForm, CustomCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'phone_number', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + ( (None, {'fields' : ('phone_number', )}),)
    add_fieldsets = UserAdmin.add_fieldsets + ( (None, {'fields' : ('phone_number','email',)}),)
 
    list_display_links = ['username']
admin.site.register(CustomUser, CustomUserAdmin)