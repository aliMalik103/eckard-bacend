# Generated by Django 4.1.4 on 2023-01-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eckard_api', '0018_cashflow_remove_project_account_projectproduction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashflow',
            name='decline',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='cashflow',
            name='gasPrice',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='cashflow',
            name='noOfMonths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cashflow',
            name='oilPrice',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=12, null=True),
        ),
    ]
