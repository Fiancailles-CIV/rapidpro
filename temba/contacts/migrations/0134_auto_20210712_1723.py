# Generated by Django 2.2.20 on 2021-07-12 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0133_auto_20210622_1824"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactgroup",
            name="name",
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name="contactgroup",
            name="query",
            field=models.TextField(null=True),
        ),
    ]