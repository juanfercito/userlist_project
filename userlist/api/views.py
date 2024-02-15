from rest_framework import viewsets

# pylint: disable=import-error
from userlist.models import Usuario
from userlist.api.serializer import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
