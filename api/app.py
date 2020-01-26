import os

from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from starlette.middleware.cors import CORSMiddleware

from .schema import schema

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Starlette(debug=True)
app.add_middleware(CORSMiddleware, allow_origins=["*"])


app.add_route("/graph/", GraphQLApp(schema=schema))
