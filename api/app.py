import os

from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware

from .views import CourseListView, CourseDetailView


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Starlette(debug=True)
app.add_middleware(CORSMiddleware, allow_origins=['*'])

app.add_route('/courses/{course_id}/', CourseDetailView)
app.add_route('/courses/', CourseListView)
