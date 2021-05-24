from django.db import models


class UfsModel(models.Model):
    UF = models.CharField(max_length=2)
    UF_detalhes = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.UF


class CidadesModel(models.Model):
    nome = models.CharField(max_length=250)
    UF = models.ForeignKey(UfsModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class UsuariosModel(models.Model):
    nome = models.CharField(max_length=250)
    cidade = models.ForeignKey(CidadesModel, on_delete=models.CASCADE, null=True, blank=True)