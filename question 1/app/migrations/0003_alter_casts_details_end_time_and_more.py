# Generated by Django 4.1.7 on 2023-02-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_model_brand_alter_casts_details_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casts_details',
            name='end_time',
            field=models.DurationField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='casts_details',
            name='start_time',
            field=models.DurationField(default='00:00:00'),
        ),
    ]
