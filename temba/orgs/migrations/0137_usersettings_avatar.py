# Generated by Django 4.2.8 on 2024-01-31 04:01

import django.core.files.storage
from django.db import migrations, models

import temba.utils.fields


class Migration(migrations.Migration):
    dependencies = [
        ("orgs", "0136_export_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersettings",
            name="avatar",
            field=models.ImageField(
                null=True,
                storage=django.core.files.storage.FileSystemStorage(),
                upload_to=temba.utils.fields.UploadToIdPathAndRename("avatars/"),
            ),
        ),
    ]
