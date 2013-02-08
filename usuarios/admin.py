from django.contrib import admin
from usuarios.forms import UsuarioForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from usuarios.models import Usuario


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UsuarioForm
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',
'email')}),
        ('Permissions', {'fields': ()}),
        ('Important dates', {'fields': ()}),
        ('Groups', {'fields': ()}),
    )
    filter_horizontal = ()
    list_filter = ()

admin.site.register(Usuario, MyUserAdmin)
admin.site.unregister(Group)
