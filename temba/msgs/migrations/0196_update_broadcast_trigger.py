# Generated by Django 4.0.7 on 2022-10-19 16:51

from django.db import migrations

SQL = """
----------------------------------------------------------------------
-- Determines the (mutually exclusive) system label for a broadcast record
----------------------------------------------------------------------
CREATE OR REPLACE FUNCTION temba_broadcast_determine_system_label(_broadcast msgs_broadcast) RETURNS CHAR(1) AS $$
BEGIN
  IF _broadcast.schedule_id IS NOT NULL AND _broadcast.is_active = TRUE THEN
    RETURN 'E';
  END IF;

  RETURN NULL; -- does not match any label
END;
$$ LANGUAGE plpgsql;
"""


class Migration(migrations.Migration):

    dependencies = [
        ("msgs", "0195_update_broadcast_is_active"),
    ]

    operations = [migrations.RunSQL(SQL)]
