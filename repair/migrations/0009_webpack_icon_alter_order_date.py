# Generated by Django 4.1.3 on 2022-12-10 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0008_alter_order_date_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpack',
            name='icon',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 10, 21, 16, 1, 846820)),
        ),
    ]
