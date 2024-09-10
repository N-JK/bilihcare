# Generated by Django 4.1.3 on 2022-12-12 10:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repair', '0020_apply_approved_alter_apply_date_alter_category_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='apply',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 12, 13, 7, 3, 66300)),
        ),
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 12, 13, 7, 3, 69231)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 12, 13, 7, 3, 63275)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 12, 13, 7, 3, 70323)),
        ),
    ]
