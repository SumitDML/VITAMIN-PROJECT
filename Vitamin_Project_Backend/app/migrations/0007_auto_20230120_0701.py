
from __future__ import unicode_literals
from django.db import migrations


def load_app_from_sql():
    import os
    sql_statements = open(os.path.join('app/sql/AllergyAndSpices.sql'), 'r').read()
    return sql_statements


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0006_auto_20230120_0700'),
    ]

    operations = [
        migrations.RunSQL(load_app_from_sql(), )
    ]
