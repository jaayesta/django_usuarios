from django.conf.urls import patterns, url, include
from views import UsuarioListView, UsuarioCreateView, \
    UsuarioUpdateView, UsuarioDeleteView

usuario_patterns = patterns(
    '',
    url(
        r'^(?P<page>[0-9]+)/(\?.*)?$',
        UsuarioListView.as_view(), name='index'),
    url(
        r'^nuevo/$',
        UsuarioCreateView.as_view(), name='nuevo'),
    url(
        r'^editar/(?P<pk>\d+)/$',
        UsuarioUpdateView.as_view(), name='editar'),
    url(
        r'^eliminar/(?P<pk>\d+)/$',
        UsuarioDeleteView.as_view(), name='eliminar'))

urlpatterns = patterns(
    '',
    url(r'^usuario/', include(usuario_patterns, namespace='usuario')),)
