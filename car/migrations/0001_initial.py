# Generated by Django 4.0.6 on 2022-07-23 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_upgrade', models.DateTimeField(auto_now=True)),
                ('price', models.CharField(max_length=255)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
