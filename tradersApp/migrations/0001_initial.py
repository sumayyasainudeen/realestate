# Generated by Django 4.1.4 on 2023-12-14 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('location', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('Features', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('property_image', models.ImageField(null=True, upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.IntegerField(default=0)),
                ('type', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('Features', models.CharField(max_length=220)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tradersApp.properties')),
            ],
        ),
        migrations.CreateModel(
            name='Tenants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('phone', models.IntegerField(default=0)),
                ('document', models.ImageField(null=True, upload_to='image/')),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rental_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('rent_date', models.DateField(null=True)),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tradersApp.tenants')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tradersApp.units')),
            ],
        ),
        migrations.AddField(
            model_name='properties',
            name='assigned_tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tradersApp.tenants'),
        ),
    ]
