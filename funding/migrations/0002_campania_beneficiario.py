# Generated by Django 4.2.11 on 2024-04-12 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campania',
            name='beneficiario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='funding.beneficiario'),
        ),
    ]