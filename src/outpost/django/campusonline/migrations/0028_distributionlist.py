# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-31 09:07
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


class Migration(migrations.Migration):

    forward = [
        """
        CREATE FOREIGN TABLE "campusonline"."verteilerliste" (
            PROFIL_NR numeric,
            PROFIL_NAME varchar
        )
        SERVER sqlalchemy OPTIONS (
            tablename 'VERTEILERLISTE_V',
            db_url '{}'
        );
        """.format(settings.MULTICORN.get('campusonline')),
        """
        CREATE FOREIGN TABLE "campusonline"."verteilerliste_person" (
            PROFIL_NR numeric,
            PERS_NR numeric
        )
        SERVER sqlalchemy OPTIONS (
            tablename 'VERTEILERLISTE_PERSON_V',
            db_url '{}'
        );
        """.format(settings.MULTICORN.get('campusonline')),
        """
        CREATE MATERIALIZED VIEW "public"."campusonline_distributionlist" AS SELECT
            profil_nr::integer AS id,
            profil_name AS name
        FROM "campusonline"."verteilerliste"
        WITH DATA;
        """,
        """
        CREATE MATERIALIZED VIEW "public"."campusonline_distributionlist_person" AS SELECT
            profil_nr::integer AS distributionlist_id,
            pers_nr::integer AS person_id
        FROM "campusonline"."verteilerliste_person"
        WITH DATA;
        """,
    ]
    reverse = [
        """
        DROP MATERIALIZED VIEW IF EXISTS "public"."campusonline_distributionlist_person";
        """,
        """
        DROP MATERIALIZED VIEW IF EXISTS "public"."campusonline_distributionlist";
        """,
        """
        DROP FOREIGN TABLE IF EXISTS "campusonline"."verteilerliste_person";
        """,
        """
        DROP FOREIGN TABLE IF EXISTS "campusonline"."verteilerliste";
        """,
    ]

    dependencies = [
        ('campusonline', '0027_indices'),
    ]

    operations = [
        migrations.RunSQL(
            forward,
            reverse
        )
    ]
