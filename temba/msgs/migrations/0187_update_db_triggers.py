# Generated by Django 4.0.7 on 2022-09-13 18:42

from django.db import migrations

SQL = """
DROP TRIGGER temba_channelevent_on_change_trg ON channels_channelevent;
DROP FUNCTION temba_channelevent_is_call(channels_channelevent);
DROP FUNCTION temba_channelevent_on_change();
"""


class Migration(migrations.Migration):

    dependencies = [
        ("msgs", "0186_msg_log_uuids"),
        ("sql", "0004_squashed"),
    ]

    operations = [migrations.RunSQL(SQL)]