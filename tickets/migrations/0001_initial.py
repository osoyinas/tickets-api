# Generated by Django 4.2.5 on 2023-09-25 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]