# Generated by Django 3.2.1 on 2021-05-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210505_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='fare_per_km',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='luggage_capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='number_of_seat',
            field=models.IntegerField(),
        ),
    ]