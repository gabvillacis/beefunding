# Generated by Django 4.2.11 on 2024-04-13 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0004_alter_beneficiario_fecha_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formapago',
            name='usuarios',
        ),
        migrations.AlterField(
            model_name='campania',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
