# Generated by Django 2.2.8 on 2020-04-21 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_auto_20200421_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_set', to='Post.Comment'),
        ),
    ]
