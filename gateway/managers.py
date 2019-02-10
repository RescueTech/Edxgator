"""
Stores, retrieves, and inspects courses only in the case of syncing from outside sources
"""
from datetime import datetime
from pymongo import MongoClient


class CourseSyncManager:

    def __init__(self):
        self.connection = MongoClient()
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

    def sync(self, courses):
        if type(courses) is not list:
            courses = [courses]
        self.new_courses += len(courses)
        self._create_or_update_courses(courses)
