# Generated by Django 3.2.7 on 2021-09-26 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile',
        ),
    ]
