from django.forms import ModelForm
from usuarios.models import Usuario
# from django.contrib.localflavor.cl.forms import CLRutField


class UsuarioForm(ModelForm):
    # rut = CLRutField()

    class Meta:
        model = Usuario
