from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    siap = models.CharField(max_length=7)

    def __str__(self):
        return self.nome