# Generated by Django 2.2.12 on 2020-05-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200514_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default='abcd', max_length=20),
            preserve_default=False,
        ),
    ]
