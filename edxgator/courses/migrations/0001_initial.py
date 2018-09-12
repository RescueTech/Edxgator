# Generated by Django 2.1.1 on 2018-09-12 06:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('number', models.CharField(blank=True, default='', max_length=15)),
                ('min_effort', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('mobile_available', models.BooleanField(blank=True, null=True)),
                ('organization', models.CharField(blank=True, default='', max_length=15)),
                ('first_enrollable_paid_seat_sku', models.CharField(blank=True, default='', max_length=20)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('enrollment_end', models.DateTimeField(blank=True, null=True)),
                ('marketing_url', models.URLField(blank=True, null=True)),
                ('type', models.CharField(blank=True, default='', max_length=20)),
                ('has_enrollable_seats', models.BooleanField(blank=True, null=True)),
                ('full_description', models.TextField(blank=True, null=True)),
                ('program_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None)),
                ('staff_uuids', django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), blank=True, default=list, size=None)),
                ('weeks_to_complete', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('short_description', models.CharField(blank=True, default='', max_length=350)),
                ('content_type', models.CharField(blank=True, default='', max_length=20)),
                ('subject_uuids', django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), blank=True, default=list, size=None)),
                ('pacing_type', models.CharField(blank=True, default='', max_length=20)),
                ('published', models.BooleanField(blank=True, null=True)),
                ('aggregation_key', models.CharField(blank=True, default='', max_length=100)),
                ('authoring_organization_uuids', django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), blank=True, default=list, size=None)),
                ('language', models.CharField(blank=True, default='', max_length=30)),
                ('enrollment_start', models.DateTimeField(blank=True, null=True)),
                ('transcript_languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, default=list, size=None)),
                ('first_enrollable_paid_seat_price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('key', models.CharField(blank=True, max_length=60, null=True)),
                ('logo_image_urls', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), blank=True, default=list, size=None)),
                ('seat_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=20), blank=True, default=list, size=None)),
                ('level_type', models.CharField(blank=True, default='', max_length=30)),
                ('max_effort', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('partner', models.CharField(blank=True, default='', max_length=20)),
                ('availability', models.CharField(blank=True, default='', max_length=30)),
            ],
        ),
    ]