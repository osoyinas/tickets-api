# Generated by Django 4.2.5 on 2023-10-01 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_person_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='time_checked',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
