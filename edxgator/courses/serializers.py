from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):

    org = serializers.CharField(source='organization')

    class Meta:
        model = Course
        fields = (
            'id', 'title', 'start', 'end', 'number', 'min_effort', 'mobile_available', 'org',
            'first_enrollable_paid_seat_sku', 'image_url', 'enrollment_end', 'marketing_url', 'type',
            'has_enrollable_seats', 'full_description', 'program_types', 'staff_uuids', 'weeks_to_complete',
            'short_description', 'content_type', 'subject_uuids', 'pacing_type', 'published', 'aggregation_key',
            'authoring_organization_uuids', 'language', 'enrollment_start', 'transcript_languages',
            'first_enrollable_paid_seat_price', 'key', 'logo_image_urls', 'seat_types', 'level_type', 'max_effort',
            'partner', 'availability'
        )
