# Generated by Django 5.1.2 on 2024-11-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0026_aluno_age"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aluno",
            name="age",
        ),
        migrations.AddField(
            model_name="aluno",
            name="idade",
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
