# Generated by Django 5.1.4 on 2025-01-15 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_modeloveiculo_em_producao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('cor', models.CharField(max_length=32)),
                ('ano', models.PositiveIntegerField()),
                ('km_rodados', models.PositiveIntegerField()),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='veiculos', to='core.modeloveiculo')),
            ],
            options={
                'verbose_name': 'Veículo',
                'verbose_name_plural': 'Veículos',
                'ordering': ['modelo__montadora__nome', 'modelo__nome'],
            },
        ),
    ]
