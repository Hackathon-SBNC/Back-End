# Generated by Django 5.1.2 on 2024-11-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_alter_aluno_matricula"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="email",
            field=models.EmailField(default=123, max_length=254),
            preserve_default=False,
        ),
    ]