# Generated by Django 5.1.4 on 2025-01-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Montadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('pais', models.CharField(max_length=128)),
                ('ano_funcacao', models.PositiveIntegerField()),
            ],
        ),
    ]