from django.db import models

from .aluno import Aluno
from .trimestre import Trimestre

class Observacao(models.Model):
    descricao = models.TextField()
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    trimestre = models.ForeignKey(Trimestre, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Observação"
        verbose_name_plural = "Observações"

    def __str__(self):
        return self.aluno.nome
    
