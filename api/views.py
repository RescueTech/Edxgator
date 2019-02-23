from bson import ObjectId
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from gateway.managers import course_manager


def course_serializer(course):
    course['_id'] = str(course['_id'])
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
