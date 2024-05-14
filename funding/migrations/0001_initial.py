# Generated by Django 4.2.11 on 2024-04-12 00:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('pais', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=50)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_ult_act', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Beneficiario',
                'verbose_name_plural': 'Beneficiarios',
                'db_table': 'st_beneficiarios',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=50)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_ult_act', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'db_table': 'st_categorias',
            },
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('usuarios', models.ManyToManyField(related_name='formas_pago', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Forma de Pago',
                'verbose_name_plural': 'Formas de Pago',
                'db_table': 'st_formas_pago',
            },
        ),
        migrations.CreateModel(
            name='Campania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=50)),
                ('foto', models.ImageField(upload_to='imagenes/')),
                ('monto_x_recaudar', models.DecimalField(decimal_places=2, max_digits=15)),
                ('monto_recaudado', models.DecimalField(decimal_places=2, max_digits=15)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_cierre', models.DateTimeField()),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_ult_act', models.DateTimeField(auto_now=True)),
                ('categorias', models.ManyToManyField(related_name='campanias', to='funding.categoria')),
            ],
            options={
                'verbose_name': 'Campaña',
                'verbose_name_plural': 'Campañas',
                'db_table': 'st_campanias',
            },
        ),
    ]