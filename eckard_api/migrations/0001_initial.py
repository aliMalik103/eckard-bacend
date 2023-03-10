# Generated by Django 4.1.4 on 2023-01-06 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountId', models.CharField(max_length=100, unique=True)),
                ('accountName', models.CharField(max_length=100)),
                ('notes', models.CharField(blank=True, max_length=100, null=True)),
                ('accountStatus', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=100)),
                ('mpStatus', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.CharField(max_length=100, unique=True)),
                ('totalNma', models.IntegerField(blank=True, null=True)),
                ('totalRevenue', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Tract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tractId', models.CharField(max_length=20, unique=True)),
                ('township', models.CharField(max_length=20)),
                ('range', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('royalityInterest', models.DecimalField(decimal_places=2, max_digits=50)),
                ('costPerNma', models.DecimalField(decimal_places=2, max_digits=50)),
                ('totalNma', models.DecimalField(decimal_places=10, max_digits=50)),
            ],
            options={
                'db_table': 'tract',
            },
        ),
        migrations.CreateModel(
            name='TractProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmaInProject', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eckard_api.project')),
                ('tract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eckard_api.tract')),
            ],
            options={
                'db_table': 'tract_project',
            },
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investmentAmount', models.IntegerField()),
                ('acquiredNma', models.IntegerField()),
                ('status', models.CharField(default='active', max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eckard_api.account')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eckard_api.project')),
            ],
            options={
                'db_table': 'investment',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eckard_api.contact'),
        ),
    ]
