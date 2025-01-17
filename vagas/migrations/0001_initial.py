# Generated by Django 5.1.3 on 2024-11-08 06:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50, null=True)),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', ckeditor.fields.RichTextField()),
                ('dataDeCriacao', models.DateField()),
                ('faixaSalarial', models.IntegerField()),
                ('requisitos', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
    ]
