# Generated by Django 5.1.3 on 2025-02-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_rename_phone_number_complaintregister_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintregister',
            name='place',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
