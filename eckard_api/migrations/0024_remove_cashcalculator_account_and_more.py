# Generated by Django 4.1.4 on 2023-01-30 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eckard_api', '0023_listing_immediateprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashcalculator',
            name='account',
        ),
        migrations.RemoveField(
            model_name='cashcalculator',
            name='project',
        ),
    ]
