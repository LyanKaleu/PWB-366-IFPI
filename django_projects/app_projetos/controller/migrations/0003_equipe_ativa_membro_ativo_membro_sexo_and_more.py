# Generated by Django 5.1.4 on 2025-02-05 19:51

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0002_comentario_alter_atividade_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='ativa',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='membro',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='membro',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], default='O', max_length=1),
        ),
        migrations.AddField(
            model_name='membro',
            name='telefone',
            field=models.CharField(blank=True, help_text='(99) 99999-9999', max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Telefone deve estar no formato (99) 99999-9999', regex='^\\(\\d{2}\\) \\d{5}-\\d{4}$')]),
        ),
        migrations.AddField(
            model_name='projeto',
            name='orcamento',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Orçamento'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='membro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atividades', to='controller.membro'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='equipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='membros', to='controller.equipe'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='data_final',
            field=models.DateField(verbose_name='Data de Fim'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='data_inicio',
            field=models.DateField(verbose_name='Data de Início'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.CharField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='equipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projetos', to='controller.equipe'),
        ),
    ]
