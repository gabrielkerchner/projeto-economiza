# Generated by Django 2.1 on 2019-08-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('economiza', '0003_auto_20190812_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria_nome',
            field=models.CharField(max_length=128),
        ),
    ]
