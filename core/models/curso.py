from django.db import models

class Curso(models.Model):
    descricao = models.CharField(max_length=255)     
    abreviatura = models.CharField(max_length=10, null=True, blank=True)                           

    def __str__(self):
        return self.descricao