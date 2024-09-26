# Generated by Django 5.1.1 on 2024-09-19 09:31

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerInfo',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='address')),
                ('phone', models.CharField(max_length=15, verbose_name='phone')),
                ('image', models.ImageField(upload_to='owner/profile', verbose_name='image')),
                ('bio', models.TextField(max_length=200, verbose_name='bio')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(verbose_name='')),
            ],
            options={
                'verbose_name': "Owner's Information",
                'verbose_name_plural': "Owner's Informations",
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('link', models.URLField(verbose_name='link')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.ownerinfo', verbose_name='owner')),
            ],
            options={
                'verbose_name': 'Social media',
                'verbose_name_plural': 'Social medias',
                'ordering': ['name'],
            },
        ),
    ]