# Generated by Django 3.1.7 on 2021-04-12 04:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('usuario', models.UUIDField(default=uuid.uuid4)),
                ('rua', models.CharField(max_length=255)),
                ('complemento1', models.CharField(max_length=255)),
                ('complemento2', models.CharField(blank=True, max_length=255, null=True)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
                ('ponto_referencia', models.TextField(blank=True, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
