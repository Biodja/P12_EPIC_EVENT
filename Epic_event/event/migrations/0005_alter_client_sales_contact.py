# Generated by Django 4.1.4 on 2023-02-06 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_alter_eventstatus_status_alter_usertype_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='event.profil'),
            preserve_default=False,
        ),
    ]