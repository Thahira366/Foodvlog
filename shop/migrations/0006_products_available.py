# Generated by Django 2.2 on 2022-11-03 06:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_merge_20221102_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]