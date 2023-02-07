# Generated by Django 4.1.4 on 2023-01-30 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eckard_api', '0024_remove_cashcalculator_account_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='account',
        ),
        migrations.AddField(
            model_name='offer',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eckard_api.contact'),
        ),
    ]
