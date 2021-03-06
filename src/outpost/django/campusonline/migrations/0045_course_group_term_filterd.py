# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-15 13:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    ops = [
        (
            '''
            DROP INDEX IF EXISTS campusonline_coursegroupterm_selection_idx;
            ''',
            '''
            CREATE INDEX campusonline_coursegroupterm_selection_idx ON "public"."campusonline_coursegroupterm" ("person_id", "room_id", "start", "end");
            ''',
        ),
        (
            '''
            DROP INDEX IF EXISTS campusonline_coursegroupterm_person_idx;
            ''',
            '''
            CREATE INDEX campusonline_coursegroupterm_person_idx ON "public"."campusonline_coursegroupterm" ("person_id");
            ''',
        ),
        (
            '''
            DROP INDEX IF EXISTS campusonline_coursegroupterm_room_idx;
            ''',
            '''
            CREATE INDEX campusonline_coursegroupterm_room_idx ON "public"."campusonline_coursegroupterm" ("room_id");
            ''',
        ),
        (
            '''
            DROP INDEX IF EXISTS campusonline_coursegroupterm_timerange_idx;
            ''',
            '''
            CREATE INDEX campusonline_coursegroupterm_timerange_idx ON "public"."campusonline_coursegroupterm" ("start", "end");
            ''',
        ),
        (
            '''
            DROP INDEX IF EXISTS campusonline_coursegroupterm_id_idx;
            ''',
            '''
            CREATE INDEX campusonline_coursegroupterm_id_idx ON "public"."campusonline_coursegroupterm" ("id");
            ''',
        ),
        (
            '''
            DROP MATERIALIZED VIEW IF EXISTS "public"."campusonline_coursegroupterm";
            ''',
            '''
            CREATE MATERIALIZED VIEW "public"."campusonline_coursegroupterm" AS SELECT
                format('%s-%s-%s', termin_nr::integer, lv_grp_nr::integer, pers_nr::integer) AS id,
                termin_nr::integer AS term,
                lv_grp_nr::integer AS coursegroup_id,
                pers_nr::integer AS person_id,
                (lv_beginn AT TIME ZONE 'Europe/Vienna') ::timestamptz AS start,
                (lv_ende AT TIME ZONE 'Europe/Vienna') ::timestamptz AS end,
                raum_nr::integer AS room_id,
                lerneinheit as title
            FROM "campusonline"."lv_grp_term"
            WITH DATA;
            ''',
        ),
        (
            '''
            CREATE MATERIALIZED VIEW "public"."campusonline_coursegroupterm" AS SELECT
                FORMAT(
                    '%s-%s-%s',
                    lgt.termin_nr::integer,
                    lgt.lv_grp_nr::integer,
                    lgt.pers_nr::integer
                ) AS id,
                lgt.termin_nr::integer AS term,
                lgt.lv_grp_nr::integer AS coursegroup_id,
                lgt.pers_nr::integer AS person_id,
                (lgt.lv_beginn AT TIME ZONE 'Europe/Vienna') ::timestamptz AS start,
                (lgt.lv_ende AT TIME ZONE 'Europe/Vienna') ::timestamptz AS end,
                lgt.raum_nr::integer AS room_id,
                lgt.lerneinheit as title
            FROM "campusonline"."lv_grp_term" lgt
            INNER JOIN "campusonline"."personen" p
            ON lgt.pers_nr::integer = p.pers_nr::integer
            WITH DATA;
            ''',
            '''
            DROP MATERIALIZED VIEW IF EXISTS "public"."campusonline_coursegroupterm";
            ''',
        ),
        (
            '''
            CREATE INDEX campusonline_coursegroupterm_selection_idx ON "public"."campusonline_coursegroupterm" ("person_id", "room_id", "start", "end");
            ''',
            '''
            DROP INDEX IF EXISTS campusonline_coursegroupterm_selection_idx;
            ''',
        ),
        (
            '''
            CREATE INDEX campusonline_coursegroupterm_person_idx ON "public"."campusonline_coursegroupterm" ("person_id");
            ''',
            '''
            DROP INDEX IF EXISTS campusonline_coursegroupterm_person_idx;
            ''',
        ),
        (
            '''
            CREATE INDEX campusonline_coursegroupterm_room_idx ON "public"."campusonline_coursegroupterm" ("room_id");
            ''',
            '''
            DROP INDEX IF EXISTS campusonline_coursegroupterm_room_idx;
            ''',
        ),
        (
            '''
            CREATE INDEX campusonline_coursegroupterm_timerange_idx ON "public"."campusonline_coursegroupterm" ("start", "end");
            ''',
            '''
            DROP INDEX IF EXISTS campusonline_coursegroupterm_timerange_idx;
            ''',
        ),
        (
            '''
            CREATE INDEX campusonline_coursegroupterm_id_idx ON "public"."campusonline_coursegroupterm" ("id");
            ''',
            '''
            DROP INDEX IF EXISTS campusonline_coursegroupterm_id_idx;
            ''',
        ),
    ]

    dependencies = [
        ('campusonline', '0044_auto_20190225_1708'),
    ]

    operations = [
        migrations.RunSQL(
            [forward for forward, reverse in ops],
            [reverse for forward, reverse in reversed(ops)]
        )
    ]
