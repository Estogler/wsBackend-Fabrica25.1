# Generated by Django 5.1.6 on 2025-03-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario_nome', models.CharField(max_length=50)),
                ('Usuario_moeda_atual', models.FloatField(max_length=200)),
                ('Usuario_moeda_para_conversao', models.FloatField(max_length=200)),
                ('Usuario_moeda_convertida', models.FloatField(max_length=200)),
            ],
        ),
    ]
