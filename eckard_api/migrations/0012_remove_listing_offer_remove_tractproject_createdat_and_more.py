# Generated by Django 4.1.4 on 2023-01-17 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eckard_api', '0011_project_tract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='tractproject',
            name='createdAt',
        ),
        migrations.RemoveField(
            model_name='tractproject',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='tractproject',
            name='deletedAt',
        ),
        migrations.RemoveField(
            model_name='tractproject',
            name='deletedBy',
        ),
        migrations.RemoveField(
            model_name='tractproject',
            name='isDeleted',
        ),
        migrations.RemoveField(
            model_name='tractproject',
            name='updatedAt',
        ),
        migrations.RemoveField(
            model_name='tractproject',
            name='updatedBy',
        ),
    ]
