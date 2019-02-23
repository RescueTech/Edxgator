from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):

    org = serializers.CharField(source='organization')

    class Meta:
        model = Course
        fields = (
            'id', 'title', 'start', 'end', 'number', 'min_effort', 'max_effort', 'org', 'image_url',
            'marketing_url', 'type', 'short_description', 'content_type', 'pacing_type', 'published', 'language',
            'enrollment_start', 'enrollment_end', 'level_type', 'availability'
        )
