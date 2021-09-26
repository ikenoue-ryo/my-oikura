# Generated by Django 3.2.7 on 2021-09-26 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_profile_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='プロフィール', to='myapp.profile'),
            preserve_default=False,
        ),
    ]