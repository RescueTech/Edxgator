"""
Stores, retrieves, and inspects courses only in the case of syncing from outside sources
"""
import os

import pymongo
from pymongo import MongoClient


class CourseSyncManager:
    FIELDS = {
        "image_url": 1,
        "title": 1,
        "org": 1,
        "availability": 1,
        "start": 1,
        "end": 1,
        "marketing_url": 1,
        "weeks_to_complete": 1,
        "pacing_type": 1,
    }
    def __init__(self):
        self.connection = MongoClient(os.getenv("MONGODB_URI"), retryWrites=False)
        if os.getenv("MONGODB_URI"):
            # This covers the case where DB name is provided in the URI
            self.db = self.connection.get_database()
        else:
            self.db = self.connection.edxgator
        self.course_collection = self.db["Course"]
        self.courses_could_not_be_validated = []
        self.updated_courses = 0
        self.new_courses = 0

    def _handle_course_anomalies(self):
        print("A number of {} courses couldn't be identified.".format(len(self.courses_could_not_be_validated)))
        # This so far means it has another key called uuid. We will use it here
        print("We're trying to handle anomalies now..")

        while self.courses_could_not_be_validated:
            course = self.courses_could_not_be_validated.pop()
            result = self.course_collection.replace_one({"uuid": course["uuid"]}, course, upsert=True)
            self.updated_courses += result.modified_count
            self.new_courses -= result.modified_count

    def _create_or_update_courses(self, courses):
        for course in courses:
            if 'key' not in course:
                self.courses_could_not_be_validated.append(course)
                continue
            result = self.course_collection.replace_one({"key": course["key"]}, course, upsert=True)
            self.updated_courses += result.modified_count
            self.new_courses -= result.modified_count

        if self.courses_could_not_be_validated:
            self._handle_course_anomalies()

    def all_courses(self):
        return self.course_collection.find()

    def our_suggested_courses(self):
        return self.course_collection.find(
            {
                "language": "English",
                "authoring_organizations.name": {"$ne": "Microsoft"}, "org": {"$ne" : "Microsoft"},
                "availability": {"$in": ["Upcoming", "Starting Soon", "Current"]},
                "content_type": "courserun",  # For now don't show Edx programs
                "weeks_to_complete": {"$gte": 8},
                "title": {"$regex": "^((?!AP).)*$"},
            },
            self.FIELDS
        ).sort("weeks_to_complete", pymongo.DESCENDING)

    def get_course(self, **query):
        return self.course_collection.find_one(query)

    def sync(self, courses):
        if type(courses) is not list:
            courses = [courses]
        self.new_courses += len(courses)
        self._create_or_update_courses(courses)


course_manager = CourseSyncManager()
