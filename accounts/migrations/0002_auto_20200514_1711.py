# Generated by Django 2.2.12 on 2020-05-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='userid',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
