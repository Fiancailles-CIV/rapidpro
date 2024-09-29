# Generated by Django 5.1 on 2024-09-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flows", "0336_alter_flowstart_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flowstart",
            name="status",
            field=models.CharField(
                choices=[
                    ("P", "Pending"),
                    ("Q", "Queued"),
                    ("S", "Started"),
                    ("C", "Completed"),
                    ("F", "Failed"),
                    ("I", "Interrupted"),
                ],
                default="P",
                max_length=1,
            ),
        ),
    ]