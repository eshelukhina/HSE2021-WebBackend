import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from application.query.query import Query

app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))
