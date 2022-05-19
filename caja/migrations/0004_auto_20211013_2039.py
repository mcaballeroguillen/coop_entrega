# Generated by Django 3.2.6 on 2021-10-13 20:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0003_alter_temp_caja_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_caja',
            name='Fecha',
            field=models.DateField(default=datetime.datetime(2021, 10, 13, 20, 39, 35, 470162, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='temp_caja',
            name='Usuario',
            field=models.CharField(max_length=50),
        ),
    ]