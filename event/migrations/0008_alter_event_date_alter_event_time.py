# Generated by Django 4.2.5 on 2023-10-01 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_alter_contribution_event_alter_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2023, 10, 1)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(6, 41, 22, 32160)),
        ),
    ]
