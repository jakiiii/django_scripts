# Generated by Django 3.2 on 2022-03-30 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220330_2239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('created_at',), 'verbose_name': 'Menu', 'verbose_name_plural': 'Menus'},
        ),
        migrations.AlterModelOptions(
            name='menucategory',
            options={'ordering': ('created_at',), 'verbose_name': 'Menu Category', 'verbose_name_plural': 'Menu Category'},
        ),
    ]
