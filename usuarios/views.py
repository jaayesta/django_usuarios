from django.core.urlresolvers import reverse
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm
from django.views.generic import ListView, CreateView, UpdateView, \
    DeleteView


class UsuarioListView(ListView):
    model = Usuario
    paginate_by = 20


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm

    def get_success_url(self):
        return reverse('usuarios:usuario:index', args=(1, ))


class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm

    def get_success_url(self):
        return reverse('usuarios:usuario:index', args=(1, ))


class UsuarioDeleteView(DeleteView):
    model = Usuario

    def get_success_url(self):
        return reverse('usuarios:usuario:index', args=(1, ))
