from django.contrib import admin
from usuarios.forms import UsuarioForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from usuarios.models import Usuario


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UsuarioForm
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'country', 'city', 'comuna', 'address')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ()}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
    )
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
