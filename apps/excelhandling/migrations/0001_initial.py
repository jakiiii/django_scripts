# Generated by Django 3.2 on 2021-10-17 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.PositiveIntegerField(verbose_name='START')),
                ('provider_name', models.CharField(max_length=50, verbose_name='PROVIDER NAME')),
                ('a_party', models.PositiveIntegerField(max_length='APARTY')),
                ('b_party', models.PositiveIntegerField(max_length='BPARTY')),
                ('call_duration', models.PositiveIntegerField(max_length='CALL DURATION')),
                ('usage_type', models.CharField(max_length=10, verbose_name='USAGE TYPE')),
                ('network_type', models.CharField(max_length=10, verbose_name='Network TYPE')),
                ('mcc_start_a', models.PositiveIntegerField(max_length='MCCSTARTA')),
                ('mnc_start_a', models.PositiveIntegerField(max_length='MNCSTARTA')),
                ('lac_start_a', models.PositiveIntegerField(max_length='LACSTARTA')),
                ('ci_start_a', models.PositiveIntegerField(max_length='CISTARTA')),
                ('imei', models.PositiveIntegerField(max_length='IMEI')),
                ('imsia', models.PositiveIntegerField(max_length='IMSIA')),
                ('address', models.CharField(max_length=250, verbose_name='ADDRESS')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User Information',
                'verbose_name_plural': 'User Information',
                'db_table': 'user_information',
                'ordering': ['-created_at'],
            },
        ),
    ]
