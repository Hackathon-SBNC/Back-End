# Generated by Django 5.1.2 on 2024-11-29 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_curso_abreviatura"),
    ]

    operations = [
        migrations.AlterField(
            model_name="turma",
            name="numeracao",
            field=models.IntegerField(
                blank=True,
                default=None,
                null=True,
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)],
            ),
        ),
    ]
