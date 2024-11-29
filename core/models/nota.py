from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .disciplina import Disciplina


class Nota(models.Model):
    nota = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])      
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"

    def __str__(self):
        return f'{self.nota} - {self.disciplina.nome}'