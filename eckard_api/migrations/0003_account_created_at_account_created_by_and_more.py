# Generated by Django 4.1.4 on 2023-01-09 10:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eckard_api', '0002_alter_investment_acquirednma_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='account_created_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='account',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='deleted_by',
            field=models.ForeignKey(blank=True, db_column='deleted_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='account_deleted_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='account',
            name='updated_by',
            field=models.ForeignKey(blank=True, db_column='updated_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='account_updated_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contact_created_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='contact',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='deleted_by',
            field=models.ForeignKey(blank=True, db_column='deleted_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contact_deleted_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='contact',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated_by',
            field=models.ForeignKey(blank=True, db_column='updated_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contact_updated_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='investment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investment',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='investment_created_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='investment',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='deleted_by',
            field=models.ForeignKey(blank=True, db_column='deleted_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='investment_deleted_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='investment',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='investment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='updated_by',
            field=models.ForeignKey(blank=True, db_column='updated_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='investment_updated_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='project_created_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='project',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='deleted_by',
            field=models.ForeignKey(blank=True, db_column='deleted_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='project_deleted_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='project',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='project',
            name='updated_by',
            field=models.ForeignKey(blank=True, db_column='updated_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='project_updated_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='tract',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tract',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tract_created_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='tract',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tract',
            name='deleted_by',
            field=models.ForeignKey(blank=True, db_column='deleted_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tract_deleted_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='tract',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tract',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tract',
            name='updated_by',
            field=models.ForeignKey(blank=True, db_column='updated_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tract_updated_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='tractproject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tractproject',
            name='created_by',
            field=models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='track_project_created_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='tractproject',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tractproject',
            name='deleted_by',
            field=models.ForeignKey(blank=True, db_column='deleted_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='track_project_deleted_by', to='eckard_api.contact'),
        ),
        migrations.AddField(
            model_name='tractproject',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tractproject',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tractproject',
            name='updated_by',
            field=models.ForeignKey(blank=True, db_column='updated_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='track_project_updated_by', to='eckard_api.contact'),
        ),
    ]
