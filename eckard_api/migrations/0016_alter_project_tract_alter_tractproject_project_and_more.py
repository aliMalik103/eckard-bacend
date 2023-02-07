# Generated by Django 4.1.4 on 2023-01-17 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eckard_api', '0015_alter_listingoffer_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tract',
            field=models.ManyToManyField(blank=True, related_name='tracts', through='eckard_api.TractProject', to='eckard_api.tract'),
        ),
        migrations.AlterField(
            model_name='tractproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracts', to='eckard_api.project'),
        ),
        migrations.AlterField(
            model_name='tractproject',
            name='tract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='eckard_api.tract'),
        ),
    ]
