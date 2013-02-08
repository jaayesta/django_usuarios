from django.contrib import admin
from usuarios.forms import UsuarioForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from usuarios.models import Usuario

username = models.CharField(max_length=255, unique=True, db_index=True)
email = models.EmailField(max_length=255, unique=True)
first_name = models.CharField(max_length=255, blank=True)
last_name = models.CharField(max_length=255, blank=True)
is_active = models.BooleanField(default=True)
is_admin = models.BooleanField(default=False)
country = models.CharField(max_length=255, blank=True)
city = models.CharField(max_length=255, blank=True)
comuna = models.CharField(max_length=255, blank=True)
address = models.CharField(max_length=255, blank=True)
cellphone = models.IntegerField(blank=True, null=True)
profile_picture = models.ImageField(
    upload_to='pictures', blank=True, null=True)
birthdate = models.DateField(blank=True, null=True)
coordinates = models.CharField(max_length=255, blank=True)



class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UsuarioForm
	list_display = ('email', 'firs_name', 'last_name', 'is_admin', 'country', 'city', 'comuna', 'address', '')
	    list_filter = ('is_admin',)
	    fieldsets = (
	        (None, {'fields': ('email', 'password')}),
	        ('Personal info', {'fields': ('date_of_birth',)}),
	        ('Permissions', {'fields': ('is_admin',)}),
	        ('Important dates', {'fields': ('last_login',)}),
	    )
	    add_fieldsets = (
	        (None, {
	            'classes': ('wide',),
	            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
	        ),
	    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Usuario, MyUserAdmin)
admin.site.unregister(Group)
