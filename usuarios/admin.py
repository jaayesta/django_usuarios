from django.contrib import admin
from usuarios.forms import UsuarioForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from usuarios.models import Usuario

class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UsuarioForm
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Usuario, MyUserAdmin)
admin.site.unregister(Group)
