# Generated by Django 4.2.11 on 2024-04-13 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0003_formapago_fecha_registro_formapago_fecha_ult_act'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiario',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
