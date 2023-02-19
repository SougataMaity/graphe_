# Generated by Django 4.1.7 on 2023-02-19 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=30)),
                ('brand_age', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='create_movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=200)),
                ('movie_duration', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'New Movie',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=30)),
                ('model_age', models.CharField(max_length=250)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='casts_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast_name', models.CharField(max_length=300)),
                ('cast_gender', models.BooleanField(choices=[(0, 'Male'), (1, 'Female')])),
                ('cast_character', models.CharField(max_length=500)),
                ('dialouge', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('movie_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.create_movie')),
            ],
            options={
                'verbose_name_plural': 'Cast and Dialouge',
            },
        ),
    ]