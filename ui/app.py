import os

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Starlette(debug=True, template_directory=BASE_DIR + "/templates")
app.mount('/static', StaticFiles(directory=BASE_DIR + "/static"))


@app.route('/courses/')
def homepage(request):
    template = app.get_template('courses.html')
    content = template.render(request=request)
    return HTMLResponse(content)
