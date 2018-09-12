from django.db import models
from django.contrib.postgres.fields import ArrayField


class Course(models.Model):
    title = models.CharField(max_length=100)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    number = models.CharField(max_length=15, default='', blank=True)
    min_effort = models.PositiveSmallIntegerField(null=True, blank=True)
    mobile_available = models.BooleanField(null=True, blank=True)
    organization = models.CharField(max_length=15, default='', blank=True)
    first_enrollable_paid_seat_sku = models.CharField(max_length=20, default='', blank=True)
    image_url = models.URLField(null=True, blank=True)
    enrollment_end = models.DateTimeField(null=True, blank=True)
    marketing_url = models.URLField(null=True, blank=True)
    type = models.CharField(max_length=20, default='', blank=True)
    has_enrollable_seats = models.BooleanField(null=True, blank=True)
    full_description = models.TextField(null=True, blank=True)
    program_types = ArrayField(
        models.CharField(max_length=100),
        default=list, blank=True
    )
    staff_uuids = ArrayField(
        models.UUIDField(),
        default=list, blank=True
    )
    weeks_to_complete = models.PositiveSmallIntegerField(null=True, blank=True)
    short_description = models.CharField(max_length=350, default='', blank=True)
    content_type = models.CharField(max_length=20, default='', blank=True)
    subject_uuids = ArrayField(
        models.UUIDField(),
        default=list, blank=True
    )
    pacing_type = models.CharField(max_length=20, default='', blank=True)
    published = models.BooleanField(null=True, blank=True)
    aggregation_key = models.CharField(max_length=100, default='', blank=True)
    authoring_organization_uuids = ArrayField(
        models.UUIDField(),
        default=list, blank=True
    )
    language = models.CharField(max_length=30, default='', blank=True)
    enrollment_start = models.DateTimeField(null=True, blank=True)
    transcript_languages = ArrayField(
        models.CharField(max_length=30),
        default=list, blank=True
    )
    first_enrollable_paid_seat_price = models.PositiveSmallIntegerField(null=True, blank=True)
    key = models.CharField(max_length=60, null=True, blank=True)
    logo_image_urls = ArrayField(
        models.URLField(),
        default=list, blank=True
    )
    seat_types = ArrayField(
        models.CharField(max_length=20, default=''),
        default=list, blank=True
    )
    level_type = models.CharField(max_length=30, default='', blank=True)
    max_effort = models.PositiveSmallIntegerField(null=True, blank=True)
    partner = models.CharField(max_length=20, default='', blank=True)
    availability = models.CharField(max_length=30, default='', blank=True)
