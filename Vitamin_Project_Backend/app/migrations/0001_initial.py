# Generated by Django 4.1.5 on 2023-01-13 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TabChild',
            fields=[
                ('tab_child_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'tab_childs',
            },
        ),
        migrations.CreateModel(
            name='Tabs',
            fields=[
                ('tab_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'tabs',
            },
        ),
        migrations.CreateModel(
            name='ZipCodes',
            fields=[
                ('zip_code', models.CharField(editable=False, max_length=5, primary_key=True, serialize=False)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'db_table': 'zip_codes',
            },
        ),
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('LatitudeMin', models.FloatField()),
                ('LatitudeMax', models.FloatField()),
                ('NorthSouth', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'zones',
            },
        ),
        migrations.CreateModel(
            name='TabChildMappings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tabs', to='app.tabs')),
                ('tab_child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='app.tabchild')),
            ],
            options={
                'db_table': 'tab_child_mappings',
            },
        ),
        migrations.AddField(
            model_name='tabchild',
            name='tab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='app.tabs'),
        ),
        migrations.CreateModel(
            name='SunshineAvailability',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Month', models.IntegerField()),
                ('Strength', models.IntegerField()),
                ('ZoneID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strengths', to='app.zones')),
            ],
            options={
                'db_table': 'sunshine_availability',
            },
        ),
    ]