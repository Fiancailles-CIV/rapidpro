# Generated by Django 4.2.3 on 2023-11-01 16:36

from django.db import migrations


def delete_scheduleless_schedules(apps, schema_editor):  # pragma: no cover
    Trigger = apps.get_model("triggers", "Trigger")

    num_deleted, _ = Trigger.objects.filter(trigger_type="S", schedule=None).delete()
    if num_deleted:
        print(f"Deleted {num_deleted} schedule triggers without a schedule")


def reverse(apps, schema_editor):  # pragma: no cover
    pass


class Migration(migrations.Migration):
    dependencies = [("triggers", "0036_alter_trigger_priority")]

    operations = [migrations.RunPython(delete_scheduleless_schedules, reverse)]
