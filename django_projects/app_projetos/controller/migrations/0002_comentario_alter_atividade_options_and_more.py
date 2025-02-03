# Generated by Django 5.1.4 on 2025-02-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=500, verbose_name='Comentário')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Data Criação')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Última atuualização')),
            ],
        ),
        migrations.AlterModelOptions(
            name='atividade',
            options={'ordering': ['data_limite', 'nome'], 'verbose_name': 'Atividade', 'verbose_name_plural': 'Atividades'},
        ),
        migrations.AlterModelOptions(
            name='equipe',
            options={'ordering': ['nome'], 'verbose_name': 'Equipe', 'verbose_name_plural': 'Equipes'},
        ),
        migrations.AlterModelOptions(
            name='membro',
            options={'ordering': ['nome'], 'verbose_name': 'Membro', 'verbose_name_plural': 'Membros'},
        ),
        migrations.AlterModelOptions(
            name='projeto',
            options={'ordering': ['nome'], 'verbose_name': 'Projeto', 'verbose_name_plural': 'Projetos'},
        ),
    ]
