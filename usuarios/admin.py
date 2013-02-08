from django.contrib import admin
from usuarios.forms import UsuarioForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from usuarios.models import Usuario

class MyUserAdmin(UserAdmin):
	form = UserChangeForm
	add_form = UsuarioForm
	list_display = ('email', 'first_name', 'last_name', 'is_admin', 'country', 'city', 'comuna', 'address',)
	list_filter = ('is_admin',)
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': ('first_name', 'last_name', 'country', 'city', 'comuna', 'address',)}),
		('Permissions', {'fields': ('is_admin',)}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'country', 'city', 'comuna', 'address', 'birthdate', 'password1', 'password2')}
		),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(Usuario, MyUserAdmin)
admin.site.unregister(Group)
