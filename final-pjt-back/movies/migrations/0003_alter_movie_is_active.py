# Generated by Django 3.2.12 on 2022-05-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220523_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='is_active',
            field=models.IntegerField(),
        ),
    ]
