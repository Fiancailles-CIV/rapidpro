# This is a dummy migration which will be implemented in the next release

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0183_squashed"),
        ("channels", "0179_squashed"),
    ]

    operations = []
