# Generated by Django 4.2.1 on 2023-06-06 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_restaurant_end_time_alter_restaurant_open_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_name',
            new_name='name',
        ),
    ]
