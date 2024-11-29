from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .curso import Curso


class Turma(models.Model):
    numeracao = models.IntegerField(
        default=None,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(3)
        ]
    )
    ano = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(3)
        ]
    )
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

    def __str__(self):
        numeracao_str = str(self.numeracao) if self.numeracao is not None else ""
        return f"{self.ano}{self.curso.abreviatura}{numeracao_str}"
