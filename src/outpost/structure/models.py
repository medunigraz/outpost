from django.db import models

from outpost.base.fields import LowerCaseCharField


class Organization(models.Model):
    campusonline = models.ForeignKey(
        'campusonline.Organization',
        models.CASCADE,
        db_constraint=False,
        related_name='+'
    )
    color = LowerCaseCharField(
        max_length=6,
        default='007b3c'
    )
    office = models.ForeignKey(
        'geo.Room',
        null=True,
        blank=True
    )
    hidden = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = (
            'campusonline__name',
        )

    def __str__(self):
        return self.campusonline.name


class Person(models.Model):
    campusonline = models.ForeignKey(
        'campusonline.Person',
        models.CASCADE,
        db_constraint=False,
        related_name='+'
    )
    room = models.ForeignKey(
        'geo.Room',
        null=True,
        blank=True
    )
    hidden = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = (
            'campusonline__last_name',
            'campusonline__first_name',
        )

    def __str__(self):
        return '{c.last_name}, {c.first_name}'.format(c=self.campusonline)