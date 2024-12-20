# Generated by Django 5.1.2 on 2024-11-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_observacao_options_alter_observacao_descricao"),
    ]

    operations = [
        migrations.CreateModel(
            name="Nota",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nota", models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                "verbose_name": "Nota",
                "verbose_name_plural": "Notas",
            },
        ),
    ]
