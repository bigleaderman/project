# Generated by Django 3.2.12 on 2022-05-26 05:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='kind',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
    ]
