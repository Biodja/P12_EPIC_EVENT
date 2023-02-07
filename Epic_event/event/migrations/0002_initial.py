# Generated by Django 4.1.4 on 2023-02-06 16:17

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=20)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
                ('amount', models.FloatField()),
                ('payment_due', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.client')),
            ],
        ),
        migrations.CreateModel(
            name='EventStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(1, 'commercial'), (2, 'support')], max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.usertype')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now_add=True)),
                ('event_status', models.CharField(max_length=20)),
                ('attendees', models.IntegerField()),
                ('event_date', models.DateTimeField()),
                ('notes', models.TextField()),
                ('client', models.ManyToManyField(related_name='client_contract', through='event.Contract', to='event.client')),
                ('support_contact', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='event.profil')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
        migrations.AddField(
            model_name='contract',
            name='sales_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.profil'),
        ),
        migrations.AddField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.profil'),
        ),
    ]
