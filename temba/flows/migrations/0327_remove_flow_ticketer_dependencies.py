# Generated by Django 4.2.8 on 2024-01-03 15:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("flows", "0326_index_cleanup"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="flow",
            name="ticketer_dependencies",
        ),
    ]