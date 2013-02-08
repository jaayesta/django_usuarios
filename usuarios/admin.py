from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

MyUserAdmin(UserAdmin):
  add_form = UserCreationForm


User = get_user_model()
admin.site.register(User, MyUserAdmin)
