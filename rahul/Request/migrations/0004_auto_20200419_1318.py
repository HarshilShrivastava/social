# Generated by Django 2.2.8 on 2020-04-19 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Request', '0003_remove_request_rejected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmed',
            name='Timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
