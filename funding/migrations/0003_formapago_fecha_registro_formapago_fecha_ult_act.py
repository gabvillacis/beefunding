# Generated by Django 4.2.11 on 2024-04-13 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0002_campania_beneficiario'),
    ]

    operations = [
        migrations.AddField(
            model_name='formapago',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='formapago',
            name='fecha_ult_act',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
