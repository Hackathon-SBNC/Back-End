# Generated by Django 5.1.2 on 2024-11-29 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0025_aluno_responsavel"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="age",
            field=models.IntegerField(default=0),
        ),
    ]
