# This is a dummy migration which will be implemented in 7.3

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0170_squashed"),
        ("airtime", "0022_squashed"),
    ]

    operations = []
