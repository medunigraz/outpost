# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 12:33
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


class Migration(migrations.Migration):

    forward = [
        '''
        CREATE SCHEMA IF NOT EXISTS thesis;
        ''',
        '''
        CREATE FOREIGN TABLE "thesis"."doctoralschools" (
            id integer,
            name varchar,
            speakeremail varchar
        )
        SERVER sqlalchemy OPTIONS (
            tablename 'doctoralschools',
            db_url '{}'
        );
        '''.format(settings.MULTICORN.get('thesis')),
        '''
        CREATE FOREIGN TABLE "thesis"."disciplines" (
            id integer,
            name varchar,
            number varchar,
            thesistype varchar
        )
        SERVER sqlalchemy OPTIONS (
            tablename 'disciplines',
            db_url '{}'
        );
        '''.format(settings.MULTICORN.get('thesis')),
        '''
        CREATE FOREIGN TABLE "thesis"."users_profile" (
            id integer,
            cn varchar,
            persnr varchar,
            matriculationnumber varchar
        )
        SERVER sqlalchemy OPTIONS (
            tablename 'users_profile',
            db_url '{}'
        );
        '''.format(settings.MULTICORN.get('thesis')),
        '''
        CREATE FOREIGN TABLE "thesis"."thesis" (
            id int4,
            filename varchar,
            created timestamp,
            description text,
            dvpdf varchar,
            ethicalreviewboardstatus int4,
            locked bool,
            prerequisites text,
            processstart timestamp,
            goals text,
            hypothesis text,
            methods text,
            milestoneyear1 text,
            milestoneyear2 text,
            milestoneyear3 text,
            schedule text,
            status int4,
            topic text,
            disciplineid int4,
            doctoralschoolid int4,
            studentid int4
        )
        SERVER sqlalchemy OPTIONS (
            tablename 'thesis',
            db_url '{}'
        );
        '''.format(settings.MULTICORN.get('thesis')),
        '''
        CREATE FOREIGN TABLE "thesis"."thesis_editors" (
            id int4,
            userid int4,
            thesisid int4
        )
        SERVER sqlalchemy
        OPTIONS (
            tablename 'thesis_editors',
            db_url '{}'
        );
        '''.format(settings.MULTICORN.get('thesis')),
        '''
        CREATE VIEW "public"."thesis_doctoralschool" AS SELECT
            id,
            name,
            string_to_array(speakeremail, ';') AS emails
        FROM "thesis"."doctoralschools";
        ''',
        '''
        CREATE VIEW "public"."thesis_discipline" AS SELECT
            id,
            name,
            number,
            thesistype
        FROM "thesis"."disciplines";
        ''',
        '''
        CREATE VIEW "public"."thesis_thesis" AS SELECT
            t.id AS id,
            t.created AS created,
            t.description AS description,
            NULLIF(TRIM(t.prerequisites), '') AS prerequisites,
            t.processstart AS processstart,
            NULLIF(TRIM(t.goals), '') AS goals,
            NULLIF(TRIM(t.hypothesis), '') AS hypothesis,
            NULLIF(TRIM(t.methods), '') AS methods,
            ARRAY_REMOVE(
                ARRAY_REMOVE(
                    ARRAY[
                        t.milestoneyear1,
                        t.milestoneyear2,
                        t.milestoneyear3
                    ],
                    NULL
                ),
                ''
            ) AS milestones,
            NULLIF(TRIM(t.schedule), '') AS schedule,
            t.status AS status,
            t.topic AS topic,
            t.disciplineid AS discipline_id,
            t.doctoralschoolid AS doctoralschool_id,
            s.stud_nr::integer AS student_id
        FROM
            "thesis"."thesis" t,
            "thesis"."users_profile" up,
            "campusonline"."stud" s
        WHERE
            t.studentid = up.id AND
            up.matriculationnumber = s.stud_mnr AND
            t.locked = FALSE;
        ''',
        '''
        CREATE VIEW "public"."thesis_editor" AS SELECT
            te.id,
            te.thesisid AS thesis_id,
            up.persnr::integer AS person_id
        FROM
            "thesis"."thesis_editors" te,
            "thesis"."users_profile" up
        WHERE
            te.userid = up.id AND
            (up.persnr = '') IS NOT TRUE;
        ''',
    ]
    reverse = [
        '''
        DROP VIEW IF EXISTS "public"."thesis_editor";
        ''',
        '''
        DROP VIEW IF EXISTS "public"."thesis_thesis";
        ''',
        '''
        DROP VIEW IF EXISTS "public"."thesis_discipline";
        ''',
        '''
        DROP VIEW IF EXISTS "public"."thesis_doctoralschool";
        ''',
        '''
        DROP FOREIGN TABLE IF EXISTS "thesis"."thesis_editors";
        ''',
        '''
        DROP FOREIGN TABLE IF EXISTS "thesis"."thesis";
        ''',
        '''
        DROP FOREIGN TABLE IF EXISTS "thesis"."users_profile";
        ''',
        '''
        DROP FOREIGN TABLE IF EXISTS "thesis"."disciplines";
        ''',
        '''
        DROP FOREIGN TABLE IF EXISTS "thesis"."doctoralschools";
        ''',
    ]

    dependencies = [
        ('base', '0005_html_unescape'),
        ('campusonline', '0036_distributionlist_union'),
    ]

    operations = [
        migrations.RunSQL(
            forward,
            reverse
        )
    ]
