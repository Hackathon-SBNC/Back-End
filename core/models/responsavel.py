from django.db import models


class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Responsável"
        verbose_name_plural = "Responsáveis"

    def __str__(self):
        return self.nome
    