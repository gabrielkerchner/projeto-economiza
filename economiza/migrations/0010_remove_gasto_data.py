# Generated by Django 2.1 on 2019-08-17 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('economiza', '0009_auto_20190816_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasto',
            name='data',
        ),
    ]
