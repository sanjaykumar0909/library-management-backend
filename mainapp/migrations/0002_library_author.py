# Generated by Django 5.0.2 on 2024-02-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='author',
            field=models.CharField(null=True),
        ),
    ]
