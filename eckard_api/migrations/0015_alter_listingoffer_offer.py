# Generated by Django 4.1.4 on 2023-01-17 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eckard_api', '0014_alter_listingoffer_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingoffer',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='eckard_api.offer'),
        ),
    ]
