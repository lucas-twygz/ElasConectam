# Generated by Django 5.1.1 on 2024-11-08 20:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0002_vagas_numerodecandidatos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='candidatos',
            field=models.ManyToManyField(blank=True, related_name='vagas_inscritas', to=settings.AUTH_USER_MODEL),
        ),
    ]
