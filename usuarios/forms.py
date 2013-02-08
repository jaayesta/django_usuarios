from django.forms import ModelForm
from usuarios.models import Usuario
# from django.contrib.localflavor.cl.forms import CLRutField


class UsuarioForm(ModelForm):
    # rut = CLRutField()

    class Meta:
        model = Usuario
        
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user    
