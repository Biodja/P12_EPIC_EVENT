# Generated by Django 4.1.4 on 2023-02-01 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_eventstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_status',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='eventstatus',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
