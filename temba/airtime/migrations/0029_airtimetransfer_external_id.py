# Generated by Django 5.0.4 on 2024-06-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("airtime", "0028_airtimetransfer_uuid"),
    ]

    operations = [
        migrations.AddField(
            model_name="airtimetransfer",
            name="external_id",
            field=models.CharField(max_length=255, null=True),
        ),
    ]