# Generated by Django 4.1.4 on 2023-12-15 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradersApp', '0002_alter_properties_assigned_tenant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='units',
            old_name='category',
            new_name='property',
        ),
    ]