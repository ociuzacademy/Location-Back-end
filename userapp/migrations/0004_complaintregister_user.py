# Generated by Django 5.1.3 on 2025-02-12 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_remove_complaintregister_bin_request_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintregister',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='userapp.tbl_register'),
            preserve_default=False,
        ),
    ]
