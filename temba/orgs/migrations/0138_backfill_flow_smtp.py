# Generated by Django 4.2.8 on 2024-02-06 16:29

from django.db import migrations


def backfill_flow_smtp(apps, schema_editor):
    Org = apps.get_model("orgs", "Org")
    num_updated = 0

    for org in Org.objects.filter(is_active=True, config__has_key="smtp_server"):
        smtp_server = org.config["smtp_server"]
        if smtp_server:
            org.flow_smtp = smtp_server
            org.save(update_fields=("flow_smtp",))
            num_updated += 1

    if num_updated:
        print(f"Updated {num_updated} orgs with custom SMTP settings")


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("orgs", "0137_org_flow_smtp")]

    operations = [migrations.RunPython(backfill_flow_smtp, reverse)]
