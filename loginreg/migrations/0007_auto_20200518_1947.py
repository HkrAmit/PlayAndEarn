# Generated by Django 2.2.12 on 2020-05-18 19:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0006_auto_20200518_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_player',
            name='exp_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 18, 19, 52, 44, 215929)),
        ),
    ]
