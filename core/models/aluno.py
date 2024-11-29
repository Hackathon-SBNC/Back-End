from django.db import models
from django.core.validators import MinLengthValidator

from .turma import Turma
from .responsavel import Responsavel


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    matricula = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(10)
        ]       
)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.PROTECT)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome