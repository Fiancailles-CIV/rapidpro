# Generated by Django 4.1.9 on 2023-06-26 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("channels", "0165_remove_channellog_call_remove_channellog_msg"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="channellog",
            name="channels_log_error_created",
        ),
        migrations.AlterField(
            model_name="channellog",
            name="channel",
            field=models.ForeignKey(
                db_index=False, on_delete=django.db.models.deletion.PROTECT, related_name="logs", to="channels.channel"
            ),
        ),
        migrations.AddIndex(
            model_name="channellog",
            index=models.Index(fields=["channel", "-created_on"], name="channellogs_by_channel"),
        ),
    ]