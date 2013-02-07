from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from usuarios.models import Usuario


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()


class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
        (None, {'fields': [('username', 'password'), ]}),
        (u'Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        (u'Permissions', {'fields': (
            'is_active', 'is_admin',
            )}),
        (u'Important dates', {'fields': ('last_login', 'birthdate')}),)

admin.site.register(Usuario, MyUserAdmin)
