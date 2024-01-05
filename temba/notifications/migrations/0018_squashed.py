# Generated by Django 4.2.8 on 2024-01-05 15:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("orgs", "0133_squashed"),
        ("tickets", "0057_squashed"),
        ("msgs", "0254_squashed"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notifications", "0017_squashed"),
        ("channels", "0182_squashed"),
        ("contacts", "0184_squashed"),
        ("flows", "0330_squashed"),
    ]

    operations = [
        migrations.AddField(
            model_name="notificationcount",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="notification_counts",
                to="orgs.org",
            ),
        ),
        migrations.AddField(
            model_name="notificationcount",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="notification_counts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="contact_export",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="notifications",
                to="contacts.exportcontactstask",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="contact_import",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="notifications",
                to="contacts.contactimport",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="incident",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="notifications",
                to="notifications.incident",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="message_export",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="notifications",
                to="msgs.exportmessagestask",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="notifications",
                to="orgs.org",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="results_export",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="notifications",
                to="flows.exportflowresultstask",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="ticket_export",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="notifications",
                to="tickets.exportticketstask",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="notifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="incident",
            name="channel",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="incidents",
                to="channels.channel",
            ),
        ),
        migrations.AddField(
            model_name="incident",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="incidents",
                to="orgs.org",
            ),
        ),
        migrations.AddIndex(
            model_name="notification",
            index=models.Index(
                condition=models.Q(("medium__contains", "U")),
                fields=["org", "user", "-created_on", "-id"],
                name="notifications_user_ui",
            ),
        ),
        migrations.AddIndex(
            model_name="notification",
            index=models.Index(
                condition=models.Q(("email_status", "P")),
                fields=["created_on"],
                name="notifications_email_pending",
            ),
        ),
        migrations.AddIndex(
            model_name="notification",
            index=models.Index(
                condition=models.Q(("is_seen", False)),
                fields=["org", "notification_type", "user"],
                name="notifications_unseen_of_type",
            ),
        ),
        migrations.AddConstraint(
            model_name="notification",
            constraint=models.UniqueConstraint(
                condition=models.Q(("is_seen", False)),
                fields=("org", "notification_type", "scope", "user"),
                name="notifications_unseen_scoped",
            ),
        ),
        migrations.AddIndex(
            model_name="incident",
            index=models.Index(
                condition=models.Q(("ended_on", None)),
                fields=["incident_type"],
                name="incidents_ongoing",
            ),
        ),
        migrations.AddIndex(
            model_name="incident",
            index=models.Index(
                condition=models.Q(("ended_on", None)),
                fields=["org", "-started_on"],
                name="incidents_org_ongoing",
            ),
        ),
        migrations.AddIndex(
            model_name="incident",
            index=models.Index(
                condition=models.Q(("ended_on__isnull", False)),
                fields=["org", "-started_on"],
                name="incidents_org_ended",
            ),
        ),
        migrations.AddConstraint(
            model_name="incident",
            constraint=models.UniqueConstraint(
                condition=models.Q(("ended_on", None)),
                fields=("org", "incident_type", "scope"),
                name="incidents_ongoing_scoped",
            ),
        ),
    ]
