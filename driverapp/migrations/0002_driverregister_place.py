# Generated by Django 5.1.3 on 2025-02-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driverapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverregister',
            name='place',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
