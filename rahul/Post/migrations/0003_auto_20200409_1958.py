# Generated by Django 2.2.8 on 2020-04-09 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20200409_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='Profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Profile.Profile'),
        ),
    ]
