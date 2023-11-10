# Generated by Django 4.2.3 on 2023-11-07 20:38

from django.db import migrations


def backfill_medium(apps, schema_editor):
    Notification = apps.get_model("notifications", "Notification")

    num_updated = 0

    while True:
        id_batch = list(Notification.objects.filter(medium=None).values_list("id", flat=True)[:1000])
        if not id_batch:
            break

        Notification.objects.filter(id__in=id_batch, email_status="N").update(medium="U")
        Notification.objects.filter(id__in=id_batch, email_status__in=("P", "S")).update(medium="UE")
        num_updated += len(id_batch)

    if num_updated:
        print(f"Backfilled medium on {num_updated} notifications")


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("notifications", "0013_notification_medium")]

    operations = [migrations.RunPython(backfill_medium, reverse)]