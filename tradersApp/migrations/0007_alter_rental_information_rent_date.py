# Generated by Django 4.1.4 on 2023-12-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradersApp', '0006_rental_information_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_information',
            name='rent_date',
            field=models.IntegerField(default=0),
        ),
    ]