# Generated by Django 3.1.6 on 2021-04-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profile_is_advertiser'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='reklame_limit',
            field=models.IntegerField(default=3),
        ),
    ]
