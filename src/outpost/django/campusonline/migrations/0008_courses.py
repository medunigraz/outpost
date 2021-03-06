# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 12:24
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('campusonline', '0007_auto_20170829_0851'),
    ]

    forward = [
        '''
        CREATE FOREIGN TABLE "campusonline"."lv" (
            LV_NR numeric,
            LV_LVNR varchar,
            LV_TITEL varchar,
            LV_TYP varchar,
            LV_TYP_LANG varchar,
            LV_STUDJAHR varchar,
            LV_SEMESTER varchar,
            SEMESTER_BEZEICHNUNG varchar
        )
        SERVER sqlalchemy OPTIONS (
            tablename 'LV_V',
            db_url '{}'
        );
        '''.format(settings.MULTICORN.get('campusonline')),
        '''
        CREATE FOREIGN TABLE "campusonline"."lv_grp" (
            GRP_NR numeric,
            LV_NR numeric,
            GRP_NAME varchar
        )
        SERVER sqlalchemy OPTIONS (
            tablename 'LV_GRP_V',
            db_url '{}'
        );
        '''.format(settings.MULTICORN.get('campusonline')),
        '''
        CREATE FOREIGN TABLE "campusonline"."lv_grp_stud" (
            GRP_NR numeric,
            STUD_NR numeric
        )
        SERVER sqlalchemy OPTIONS (
            tablename 'LV_GRP_STUD_V',
            db_url '{}'
        );
        '''.format(settings.MULTICORN.get('campusonline')),
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
        '''
        CREATE FOREIGN TABLE "campusonline"."lv_grp_term" (
            LV_GRP_NR numeric,
            PERS_NR numeric,
            TERMIN_NR numeric,
            LV_BEGINN timestamptz,
            LV_ENDE timestamptz,
            RAUM_NR numeric
        )
        SERVER sqlalchemy OPTIONS (
            tablename 'LV_GRP_TERM_V',
            db_url '{}'
        );
        '''.format(settings.MULTICORN.get('campusonline')),
        '''
        CREATE MATERIALIZED VIEW "public"."campusonline_course" AS SELECT
            lv_nr::integer AS id,
            lv_titel AS name,
            lv_typ_lang AS category,
            lv_studjahr AS year,
            lv_semester AS semester
        FROM "campusonline"."lv"
        WITH DATA;
        ''',
        '''
        CREATE MATERIALIZED VIEW "public"."campusonline_coursegroup" AS SELECT
            grp_nr::integer AS id,
            lv_nr::integer AS course_id,
            grp_name AS name
        FROM "campusonline"."lv_grp"
        WITH DATA;
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
        '''
        CREATE INDEX campusonline_student_id_idx ON "public"."campusonline_student" ("id");
        ''',
        '''
        CREATE INDEX campusonline_student_matriculation_idx ON "public"."campusonline_student" ("matriculation");
        ''',
        '''
        CREATE INDEX campusonline_student_cardid_idx ON "public"."campusonline_student" ("cardid");
        ''',
        '''
        CREATE MATERIALIZED VIEW "public"."campusonline_coursegroup_students" AS SELECT
            grp_nr::integer AS coursegroup_id,
            stud_nr::integer AS student_id
        FROM "campusonline"."lv_grp_stud"
        WITH DATA;
        ''',
        '''
        CREATE INDEX campusonline_coursegroup_students_coursegroup_id_idx ON "public"."campusonline_coursegroup_students" (coursegroup_id);
        ''',
        '''
        CREATE INDEX campusonline_coursegroup_students_student_id_idx ON "public"."campusonline_coursegroup_students" (student_id);
        ''',
        '''
        CREATE MATERIALIZED VIEW "public"."campusonline_coursegroupterm" AS SELECT
            format('%s-%s-%s', termin_nr, lv_grp_nr, pers_nr) AS id,
            termin_nr::integer AS termroom_id,
            lv_grp_nr::integer AS coursegroup_id,
            pers_nr::integer AS person_id,
            lv_beginn AS start,
            lv_ende AS end,
            raum_nr::integer AS room_id
        FROM "campusonline"."lv_grp_term"
        WITH DATA;
        ''',
        '''
        CREATE INDEX campusonline_coursegroupterm_id_idx ON "public"."campusonline_coursegroupterm" ("id");
        ''',
        '''
        CREATE INDEX campusonline_coursegroupterm_timerange_idx ON "public"."campusonline_coursegroupterm" ("start", "end");
        ''',
        '''
        CREATE INDEX campusonline_coursegroupterm_room_idx ON "public"."campusonline_coursegroupterm" ("room_id");
        ''',
        '''
        CREATE INDEX campusonline_coursegroupterm_person_idx ON "public"."campusonline_coursegroupterm" ("person_id");
        ''',
        '''
        CREATE INDEX campusonline_coursegroupterm_selection_idx ON "public"."campusonline_coursegroupterm" ("person_id", "room_id", "start", "end");
        ''',
    ]

    reverse = [
        '''
        DROP INDEX IF EXISTS campusonline_coursegroupterm_selection_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_coursegroupterm_person_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_coursegroupterm_room_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_coursegroupterm_timerange_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_coursegroupterm_id_idx;
        ''',
        '''
        DROP MATERIALIZED VIEW IF EXISTS "public"."campusonline_coursegroupterm";
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_coursegroup_students_coursegroup_id_idx;
        ''',
        '''
        CREATE INDEX campusonline_student_cardid_idx ON "public"."campusonline_student" ("cardid");
        ''',
        '''
        CREATE INDEX campusonline_student_matriculation_idx ON "public"."campusonline_student" ("matriculation");
        ''',
        '''
        CREATE INDEX campusonline_student_id_idx ON "public"."campusonline_student" ("id");
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_coursegroup_students_student_id_idx;
        ''',
        '''
        DROP MATERIALIZED VIEW IF EXISTS "public"."campusonline_coursegroup_students";
        ''',
        '''
        DROP MATERIALIZED VIEW IF EXISTS "public"."campusonline_student";
        ''',
        '''
        DROP MATERIALIZED VIEW IF EXISTS "public"."campusonline_coursegroup";
        ''',
        '''
        DROP MATERIALIZED VIEW IF EXISTS "public"."campusonline_course";
        ''',
        '''
        DROP FOREIGN TABLE IF EXISTS "campusonline"."lv_grp_term";
        ''',
        '''
        DROP FOREIGN TABLE IF EXISTS "campusonline"."stud";
        ''',
        '''
        DROP FOREIGN TABLE IF EXISTS "campusonline"."lv_grp_stud";
        ''',
        '''
        DROP FOREIGN TABLE IF EXISTS "campusonline"."lv_grp";
        ''',
        '''
        DROP FOREIGN TABLE IF EXISTS "campusonline"."lv";
        ''',
    ]
    operations = [
        migrations.RunSQL(
            forward,
            reverse
        )
    ]
