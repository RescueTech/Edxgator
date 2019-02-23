import os

from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles

from .views import CourseListView, CourseDetailView


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Starlette(debug=True, template_directory=BASE_DIR + "/templates")
app.mount('/static', StaticFiles(directory=BASE_DIR + "/static"), name='static')
app.add_route('/courses/', CourseListView)
app.add_route('/courses/{course_id}/', CourseDetailView)

