# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-10 07:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    forward = [
        '''
        DROP INDEX IF EXISTS campusonline_building_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_student_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_bulletin_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_coursegroupterm_id_idx;
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_building_id_idx ON "public"."campusonline_building" ("id");
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_floor_id_idx ON "public"."campusonline_floor" ("id");
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_room_id_idx ON "public"."campusonline_room" ("id");
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_room_category_id_idx ON "public"."campusonline_room_category" ("id");
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_bulletin_id_idx ON "public"."campusonline_bulletin" ("id");
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_course_id_idx ON "public"."campusonline_course" ("id");
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_coursegroup_id_idx ON "public"."campusonline_coursegroup" ("id");
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_coursegroupterm_id_idx ON "public"."campusonline_coursegroupterm" ("id");
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_event_id_idx ON "public"."campusonline_event" ("id");
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_organization_id_idx ON "public"."campusonline_organization" ("id");
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_person_id_idx ON "public"."campusonline_person" ("id");
        ''',
        '''
        CREATE UNIQUE INDEX campusonline_student_id_idx ON "public"."campusonline_student" ("id");
        ''',
    ]

    reverse = [
        '''
        DROP INDEX IF EXISTS campusonline_student_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_person_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_organization_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_event_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_coursegroupterm_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_coursegroup_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_course_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_bulletin_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_room_category_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_room_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_floor_id_idx;
        ''',
        '''
        DROP INDEX IF EXISTS campusonline_building_id_idx;
        ''',
        '''
        CREATE INDEX campusonline_coursegroupterm_id_idx ON "public"."campusonline_coursegroupterm" ("id");
        ''',
        '''
        CREATE INDEX campusonline_bulletin_id_idx ON "public"."campusonline_bulletin" ("id");
        ''',
        '''
        CREATE INDEX campusonline_student_id_idx ON "public"."campusonline_student" ("id");
        ''',
        '''
        CREATE INDEX campusonline_building_id_idx ON "public"."campusonline_building" ("id");
        ''',
    ]

    dependencies = [
        ('campusonline', '0017_bulletin'),
    ]

    operations = [
        migrations.RunSQL(
            forward,
            reverse
        )
    ]
