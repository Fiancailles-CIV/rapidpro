# Generated by Django 4.2.2 on 2023-07-12 19:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("channels", "0168_channel_log_policy"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="channel",
            name="bod",
        ),
    ]
