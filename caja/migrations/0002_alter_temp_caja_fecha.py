# Generated by Django 3.2.6 on 2021-10-13 20:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_caja',
            name='Fecha',
            field=models.DateField(default=datetime.datetime(2021, 10, 13, 20, 27, 6, 835335, tzinfo=utc)),
        ),
    ]
