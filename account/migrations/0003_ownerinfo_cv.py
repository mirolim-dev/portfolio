# Generated by Django 5.1.1 on 2024-09-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_ownerinfo_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerinfo',
            name='cv',
            field=models.FileField(null=True, upload_to='owner/cv'),
        ),
    ]
