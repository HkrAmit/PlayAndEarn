# Generated by Django 2.2.12 on 2020-05-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200514_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='userid',
            field=models.CharField(max_length=20),
        ),
    ]
