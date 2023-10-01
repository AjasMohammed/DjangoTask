# Generated by Django 4.2.5 on 2023-09-30 18:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_alter_event_time_contribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(18, 55, 53, 514330)),
        ),
    ]