# Generated by Django 4.0.4 on 2022-06-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flows", "0290_flowsession_flows_session_has_output_or_url"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="flowrun",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(("status__in", ("A", "W")), _negated=True), ("session__isnull", False), _connector="OR"
                ),
                name="flows_run_active_or_waiting_has_session",
            ),
        ),
    ]