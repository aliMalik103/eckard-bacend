# Generated by Django 4.1.4 on 2023-01-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eckard_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='acquiredNma',
            field=models.DecimalField(decimal_places=10, max_digits=50),
        ),
        migrations.AlterField(
            model_name='investment',
            name='investmentAmount',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='totalNma',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='totalRevenue',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='tractproject',
            name='nmaInProject',
            field=models.DecimalField(decimal_places=10, max_digits=50),
        ),
    ]