# Generated by Django 4.2.1 on 2023-06-01 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('meal_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('number_of_reservations', models.IntegerField()),
                ('price_staff', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_student', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]