# Generated by Django 5.1.2 on 2024-11-29 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_ocorrencia"),
    ]

    operations = [
        migrations.CreateModel(
            name="Responsavel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=15)),
            ],
        ),
    ]
