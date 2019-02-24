import datetime

from bson import ObjectId
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from gateway.managers import course_manager


def course_serializer(course):
    """
    Responsible for serializing a course object, and return it in the format suitable for parsing as JSON,
    and also responsible for making the presentation layer enhancement, for example, converting a datetime into a date
    object when it's needed for prettification purposes.
    This layer isn't responsible for making sure that every field is in its correct type.
        ex. don't do checks to see if the start_date is really a date.. only that it's there and not null or empty str.
    """
    course['_id'] = str(course['_id'])
    course['start'] = (course.get('start') or '').split('T')[0]
    course['end'] = (course.get('end') or '').split('T')[0]
    course['pacing_type'] = course.get('pacing_type', None)
    return course


class CourseListView(HTTPEndpoint):
    async def get(self, request):
        courses = list(map(course_serializer, course_manager.our_suggested_courses()))
        return JSONResponse(courses)


class CourseDetailView(HTTPEndpoint):
    async def get(self, request):
        _id = request.path_params['course_id']
        course = course_manager.get_course(_id=ObjectId(_id))
        course['_id'] = str(course['_id'])
        return JSONResponse(course)
