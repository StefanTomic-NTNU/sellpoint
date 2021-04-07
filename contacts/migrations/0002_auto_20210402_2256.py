# Generated by Django 3.1.6 on 2021-04-02 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0011_auto_20210326_1144'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='advertisement_id',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_id',
        ),
        migrations.AddField(
            model_name='contact',
            name='message_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='recipient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipient_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='advertisement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='advertisements.advertisement'),
        ),
    ]