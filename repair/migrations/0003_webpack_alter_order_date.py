# Generated by Django 4.1.3 on 2022-12-10 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0002_order_city_order_country_alter_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webpack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tiktok', models.CharField(blank=True, max_length=2555, null=True)),
                ('instagram', models.CharField(blank=True, max_length=2555, null=True)),
                ('facebook', models.CharField(blank=True, max_length=2555, null=True)),
                ('telegram', models.CharField(blank=True, max_length=2555, null=True)),
                ('whatsup', models.CharField(blank=True, max_length=2555, null=True)),
                ('youtube', models.CharField(blank=True, max_length=2555, null=True)),
                ('twitter', models.CharField(blank=True, max_length=2555, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('eng', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 10, 15, 23, 45, 552460)),
        ),
    ]
