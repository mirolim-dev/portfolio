# Generated by Django 5.1.1 on 2024-09-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_ghost'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerinfo',
            name='major',
            field=models.CharField(default='Software engineer', max_length=60, verbose_name='major'),
        ),
    ]