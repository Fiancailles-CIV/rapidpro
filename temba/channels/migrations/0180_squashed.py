# Generated by Django 4.2.8 on 2024-01-05 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contacts", "0183_squashed"),
        ("channels", "0179_squashed"),
    ]

    operations = [
        migrations.AddField(
            model_name="channelevent",
            name="contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channel_events",
                to="contacts.contact",
            ),
        ),
        migrations.AddField(
            model_name="channelevent",
            name="contact_urn",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channel_events",
                to="contacts.contacturn",
            ),
        ),
    ]
