from django.db import models


class Observacao(models.Model):
    descricao = models.TextField()

    class Meta:
        verbose_name = "Observação"
        verbose_name_plural = "Observações"

    def __str__(self):
        return self.descricao
    
