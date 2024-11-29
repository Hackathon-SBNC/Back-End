from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Trimestre(models.Model):
    descricao = models.CharField(max_length=10)
    ano = models.IntegerField(
        validators=[
            MinValueValidator(1950),
            MaxValueValidator(3000)
        ]
    )

    def __str__(self):
        return f'{self.descricao} - {self.ano}'