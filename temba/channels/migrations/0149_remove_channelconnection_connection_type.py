# Generated by Django 4.0.7 on 2022-09-19 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("channels", "0148_alter_channelconnection_connection_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="channelconnection",
            name="connection_type",
        ),
    ]
