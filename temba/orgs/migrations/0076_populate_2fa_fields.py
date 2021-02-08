# Generated by Django 2.2.10 on 2021-02-04 16:43

import pyotp

from django.db import migrations


def populate_2fa_fields(apps, schema_editor):
    # populate BackupToken.user
    BackupToken = apps.get_model("orgs", "BackupToken")
    for token in BackupToken.objects.filter(user=None):
        token.user = token.settings.user
        token.save(update_fields=("user",))

    # populate UserSettings.otp_secret
    UserSettings = apps.get_model("orgs", "UserSettings")
    for us in UserSettings.objects.filter(otp_secret=None):
        us.otp_secret = pyotp.random_base32()
        us.save(update_fields=("otp_secret",))


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("orgs", "0075_auto_20210204_1638"),
    ]

    operations = [
        migrations.RunPython(populate_2fa_fields, reverse),
    ]
