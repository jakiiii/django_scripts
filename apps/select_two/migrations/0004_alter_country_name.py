# Generated by Django 3.2 on 2021-10-18 08:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('select_two', '0003_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=8), size=1),
        ),
    ]
