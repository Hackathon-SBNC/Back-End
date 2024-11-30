# Generated by Django 5.1.2 on 2024-11-30 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0030_observacao_acoes"),
    ]

    operations = [
        migrations.CreateModel(
            name="Professor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("siap", models.CharField(max_length=7)),
            ],
        ),
    ]
