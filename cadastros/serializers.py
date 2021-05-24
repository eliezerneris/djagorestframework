from cadastros.models import UfsModel, CidadesModel, UsuariosModel
from rest_framework import serializers


class UfsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UfsModel
        fields = ('id','UF','UF_detalhes')


class CidadesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CidadesModel
        fields = ('id','nome','UF')


class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsuariosModel
        fields = ('id', 'nome', 'cidade')