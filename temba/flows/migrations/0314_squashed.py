# Generated by Django 4.0.8 on 2023-01-11 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("campaigns", "0051_squashed"),
        ("contacts", "0170_squashed"),
        ("flows", "0313_squashed"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ivr", "0022_squashed"),
    ]

    operations = [
        migrations.AddField(
            model_name="flowstart",
            name="calls",
            field=models.ManyToManyField(related_name="starts", to="ivr.call"),
        ),
        migrations.AddField(
            model_name="flowstart",
            name="campaign_event",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="flow_starts",
                to="campaigns.campaignevent",
            ),
        ),
        migrations.AddField(
            model_name="flowstart",
            name="contacts",
            field=models.ManyToManyField(to="contacts.contact"),
        ),
        migrations.AddField(
            model_name="flowstart",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="flow_starts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="flowstart",
            name="flow",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="starts", to="flows.flow"
            ),
        ),
        migrations.AddField(
            model_name="flowstart",
            name="groups",
            field=models.ManyToManyField(to="contacts.contactgroup"),
        ),
    ]
