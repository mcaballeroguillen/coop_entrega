# Generated by Django 3.2.6 on 2021-10-13 20:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20211013_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='Fecha_Ingreso',
            field=models.DateField(default=datetime.datetime(2021, 10, 13, 20, 39, 35, 470667, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='temp_inventario',
            name='Fecha_Ingreso',
            field=models.DateField(default=datetime.datetime(2021, 10, 13, 20, 39, 35, 470993, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='temp_inventario',
            name='Usuario',
            field=models.CharField(max_length=50),
        ),
    ]
