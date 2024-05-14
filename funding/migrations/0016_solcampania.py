# Generated by Django 4.2.11 on 2024-05-13 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0015_formapago_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolCampania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(upload_to='imagenes/')),
                ('beneficiario', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, null=True)),
                ('monto_x_recaudar', models.DecimalField(decimal_places=2, max_digits=15)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(null=True)),
                ('categorias', models.ManyToManyField(related_name='Solcampania', to='funding.categoria')),
            ],
            options={
                'verbose_name': 'SolicitudCampania',
                'verbose_name_plural': 'SolicitudCampanias',
                'db_table': 'st_solCampania',
            },
        ),
    ]
