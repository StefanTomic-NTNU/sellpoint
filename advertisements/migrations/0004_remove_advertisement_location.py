# Generated by Django 3.1.6 on 2021-02-16 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0003_auto_20210216_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='location',
        ),
    ]
