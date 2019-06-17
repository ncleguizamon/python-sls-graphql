from flask import Flask
#importamos librerias
from schema import schema

from flask_graphql import GraphQLView


app = Flask(__name__)


@app.route("/cats")
def cats():
    return "Cats"


@app.route("/dogs/<id>")
def dog(id):
    return "Dog"

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)
