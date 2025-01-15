# Generated by Django 5.1.4 on 2025-01-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_modeloveiculo_options_alter_montadora_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeloveiculo',
            name='em_producao',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='montadora',
            name='ano_fundacao',
            field=models.PositiveIntegerField(verbose_name='Ano de Fundação'),
        ),
        migrations.AlterField(
            model_name='montadora',
            name='nome',
            field=models.CharField(max_length=128, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='montadora',
            name='pais',
            field=models.CharField(max_length=128, verbose_name='País'),
        ),
    ]