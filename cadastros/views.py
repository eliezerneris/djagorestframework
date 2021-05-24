from cadastros.models import UfsModel, CidadesModel, UsuariosModel
from cadastros.serializers import UfsSerializers, CidadesSerializers, UsuariosSerializers
from rest_framework import viewsets


class Ufs(viewsets.ModelViewSet):
    queryset = UfsModel.objects.all()
    serializer_class = UfsSerializers


class Cidades(viewsets.ModelViewSet):
    queryset = CidadesModel.objects.all()
    serializer_class = CidadesSerializers


class Usuarios(viewsets.ModelViewSet):
    queryset = UsuariosModel.objects.all()
    serializer_class = UsuariosSerializers