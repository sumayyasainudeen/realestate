# Generated by Django 4.1.4 on 2023-12-14 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tradersApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='assigned_tenant',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='tradersApp.tenants'),
        ),
    ]