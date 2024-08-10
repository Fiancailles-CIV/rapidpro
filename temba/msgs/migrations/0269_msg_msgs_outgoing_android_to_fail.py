# Generated by Django 5.0.7 on 2024-08-05 18:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("channels", "0185_alter_channel_name"),
        ("contacts", "0191_contactnote"),
        ("flows", "0334_remove_flowrun_submitted_by"),
        ("msgs", "0268_trim_old_broadcasts_to_nodes"),
        ("orgs", "0144_alter_usersettings_email_verification_secret"),
        ("tickets", "0060_delete_exportticketstask"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name="msg",
            index=models.Index(
                condition=models.Q(("direction", "O"), ("is_android", True), ("status__in", ("I", "Q", "E"))),
                fields=["created_on"],
                name="msgs_outgoing_android_to_fail",
            ),
        ),
    ]
