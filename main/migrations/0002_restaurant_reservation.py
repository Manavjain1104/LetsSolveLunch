# Generated by Django 4.2.1 on 2023-06-06 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('open_time', models.TimeField(auto_now_add=True)),
                ('end_time', models.TimeField(auto_now_add=True)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.meal')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('order_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('collected', models.BooleanField(default=False)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.meal')),
            ],
        ),
    ]
