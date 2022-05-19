# Generated by Django 3.2.6 on 2021-10-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acciones_accionista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Identidad', models.CharField(max_length=15)),
                ('Num_Recibo', models.IntegerField()),
                ('Reglamento', models.FloatField()),
                ('Extaordinaria', models.FloatField()),
                ('Utilidad', models.FloatField()),
                ('Donación', models.FloatField()),
                ('Intereses', models.FloatField()),
                ('Perdidas', models.FloatField()),
                ('Total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Datos_Accionista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Identidad', models.CharField(max_length=15)),
                ('Fecha_Ingreso', models.DateField()),
                ('Fundador', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Temp_Acciones_accionista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=15)),
                ('Identidad', models.CharField(max_length=15)),
                ('Fecha', models.DateField()),
                ('Num_Recibo', models.IntegerField()),
                ('Reglamento', models.FloatField()),
                ('Extaordinaria', models.FloatField()),
                ('Utilidad', models.FloatField()),
                ('Donación', models.FloatField()),
                ('Intereses', models.FloatField()),
                ('Perdidas', models.FloatField()),
                ('Total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Temp_Datos_Accionista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=15)),
                ('Nombre', models.CharField(max_length=50)),
                ('Identidad', models.CharField(max_length=15)),
                ('Fecha_Ingreso', models.DateField()),
                ('Fundador', models.CharField(max_length=1)),
            ],
        ),
    ]
