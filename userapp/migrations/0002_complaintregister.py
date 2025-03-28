# Generated by Django 5.1.3 on 2025-02-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('ward', models.CharField(max_length=100)),
                ('location', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='complaints/')),
                ('bin_request_image', models.ImageField(blank=True, null=True, upload_to='bin_requests/')),
                ('bin', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('resolved', 'Resolved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
