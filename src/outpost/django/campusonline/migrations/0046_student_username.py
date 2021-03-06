# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-27 13:29
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


class Migration(migrations.Migration):

    ops = [
        (
            '''
            DROP INDEX IF EXISTS campusonline_student_cardid_idx;
            ''',
            '''
            CREATE INDEX campusonline_student_cardid_idx ON "public"."campusonline_student" ("cardid");
            ''',
        ),
        (
            '''
            DROP INDEX IF EXISTS campusonline_student_matriculation_idx;
            ''',
            '''
            CREATE INDEX campusonline_student_matriculation_idx ON "public"."campusonline_student" ("matriculation");
            ''',
        ),
        (
            '''
            DROP INDEX IF EXISTS campusonline_student_id_idx;
            ''',
            '''
            CREATE INDEX campusonline_student_id_idx ON "public"."campusonline_student" ("id");
            ''',
        ),
        (
            '''
            DROP MATERIALIZED VIEW IF EXISTS "public"."campusonline_student";
            ''',
            '''
            CREATE MATERIALIZED VIEW "public"."campusonline_student" AS SELECT
                stud_nr::integer AS id,
                stud_mnr AS matriculation,
                stud_famnam AS last_name,
                stud_vorname AS first_name,
                stud_akadgrad AS title,
                stud_mifare AS cardid
            FROM "campusonline"."stud"
            WITH DATA;
            ''',
        ),
        (
            '''
            DROP FOREIGN TABLE IF EXISTS "campusonline"."stud";
            ''',
            '''
            CREATE FOREIGN TABLE "campusonline"."stud" (
                STUD_NR numeric,
                STUD_MNR varchar,
                STUD_FAMNAM varchar,
                STUD_VORNAME varchar,
                STUD_AKADGRAD varchar,
                STUD_SEX varchar,
                STUD_MIFARE varchar
            )
            SERVER sqlalchemy OPTIONS (
                tablename 'STUD_V',
                db_url '{}'
            );
            '''.format(settings.MULTICORN.get('campusonline')),
        ),
        (
            '''
            CREATE FOREIGN TABLE "campusonline"."stud" (
                STUD_NR numeric,
                STUD_MNR varchar,
                STUD_FAMNAM varchar,
                STUD_VORNAME varchar,
                STUD_AKADGRAD varchar,
                STUD_SEX varchar,
                STUD_MIFARE varchar,
                STUD_BENUTZERNAME varchar
            )
            SERVER sqlalchemy OPTIONS (
                tablename 'STUD_V',
                db_url '{}'
            );
            '''.format(settings.MULTICORN.get('campusonline')),
            '''
            DROP FOREIGN TABLE IF EXISTS "campusonline"."stud";
            ''',
        ),
        (
            '''
            CREATE MATERIALIZED VIEW "public"."campusonline_student" AS SELECT
                stud_nr::integer AS id,
                stud_mnr AS matriculation,
                stud_famnam AS last_name,
                stud_vorname AS first_name,
                stud_akadgrad AS title,
                stud_mifare AS cardid,
                stud_benutzername as username
            FROM "campusonline"."stud"
            WITH DATA;
            ''',
            '''
            DROP MATERIALIZED VIEW IF EXISTS "public"."campusonline_student";
            ''',
        ),
        (
            '''
            CREATE INDEX campusonline_student_id_idx ON "public"."campusonline_student" ("id");
            ''',
            '''
            DROP INDEX IF EXISTS campusonline_student_id_idx;
            ''',
        ),
        (
            '''
            CREATE INDEX campusonline_student_matriculation_idx ON "public"."campusonline_student" ("matriculation");
            ''',
            '''
            DROP INDEX IF EXISTS campusonline_student_matriculation_idx;
            ''',
        ),
        (
            '''
            CREATE INDEX campusonline_student_cardid_idx ON "public"."campusonline_student" ("cardid");
            ''',
            '''
            DROP INDEX IF EXISTS campusonline_student_cardid_idx;
            ''',
        ),
        (
            '''
            CREATE INDEX campusonline_student_username_idx ON "public"."campusonline_student" ("username");
            ''',
            '''
            DROP INDEX IF EXISTS campusonline_student_username_idx;
            ''',
        ),
    ]

    dependencies = [
        ('campusonline', '0045_course_group_term_filterd'),
    ]

    operations = [
        migrations.RunSQL(
            [forward for forward, reverse in ops],
            [reverse for forward, reverse in reversed(ops)]
        )
    ]
