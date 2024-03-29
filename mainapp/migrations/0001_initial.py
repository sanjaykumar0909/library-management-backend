# Generated by Django 5.0.2 on 2024-02-22 14:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('bookId', models.IntegerField(primary_key=True, serialize=False)),
                ('bookName', models.CharField(max_length=30)),
                ('publishDate', models.DateTimeField()),
                ('available', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=30)),
                ('rented', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('due', models.DateTimeField()),
            ],
        ),
    ]
