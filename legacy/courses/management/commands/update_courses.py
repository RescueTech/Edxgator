import requests
import simplejson

from datetime import datetime

from django.core.management.base import BaseCommand

from edxgator.courses.models import Course
from edxgator.courses.serializers import CourseSerializer


class Command(BaseCommand):
    help = 'Reimports all courses based on the key attribute'

    def handle(self, *args, **options):
        """
        Loops through all pages in edx.org, and stores a local copy of the courses
        """
        next_page_url = "https://www.edx.org/api/v1/catalog/search?page=1&page_size=100"
        page_number = 1
        invalidated_objects = []
        while next_page_url:
            request_start_time = datetime.now()
            data = requests.get(next_page_url).json()
            request_end_time = datetime.now()
            assert 'objects' in data, data
            for course_data in data['objects']['results']:
                if not 'key' in course_data:
                    invalidated_objects.append(course_data)
                    continue

                existing_course = Course.objects.filter(key=course_data['key'])
                if existing_course.exists():
                    serializer = CourseSerializer(existing_course.get(), data=course_data)
                else:
                    serializer = CourseSerializer(data=course_data)

                valid = serializer.is_valid(raise_exception=False)
                if valid:
                    serializer.save()
                else:
                    invalidated_objects.append(course_data)
                    print("Another object that doesn't match validation found. Added to list.")
            courses_parsing_end_time = datetime.now()

            next_page_url = data['objects']['next']
            print(
                "Request for page no. {} took {} time".format(page_number, request_end_time - request_start_time) +
                "courses parsing time: {}".format(courses_parsing_end_time - request_end_time)
            )
            page_number += 1
            with open("invalidated_courses.json", mode="w+") as file:
                file.write(simplejson.dumps(invalidated_objects, indent=4))
