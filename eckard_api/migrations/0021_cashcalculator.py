# Generated by Django 4.1.4 on 2023-01-24 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eckard_api', '0020_remove_cashflow_decline_remove_cashflow_gasprice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashCalculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDeleted', models.BooleanField(blank=True, default=False, null=True)),
                ('deletedAt', models.DateTimeField(blank=True, null=True)),
                ('noOfMonths', models.IntegerField(blank=True, null=True)),
                ('decline', models.DecimalField(blank=True, decimal_places=5, max_digits=12, null=True)),
                ('oilPrice', models.DecimalField(blank=True, decimal_places=5, max_digits=12, null=True)),
                ('gasPrice', models.DecimalField(blank=True, decimal_places=5, max_digits=12, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedAt', models.DateTimeField(auto_now=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eckard_api.account')),
                ('createdBy', models.ForeignKey(blank=True, db_column='createdBy', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cash_cofig_created_by', to='eckard_api.contact')),
                ('deletedBy', models.ForeignKey(blank=True, db_column='deletedBy', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cash_cofig_deleted_by', to='eckard_api.contact')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eckard_api.project')),
                ('updatedBy', models.ForeignKey(blank=True, db_column='updatedBy', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cash_cofig_updated_by', to='eckard_api.contact')),
            ],
            options={
                'db_table': 'cash_config',
            },
        ),
    ]
