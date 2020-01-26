import os

from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from starlette.middleware.cors import CORSMiddleware

from .schema import schema

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


app = Starlette(debug=True)
# Note: without the second two options here, the OPTIONS call from Vue-Apollo client will fail for some reason!
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


app.add_route("/graph/", GraphQLApp(schema=schema))
