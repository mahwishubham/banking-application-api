import psycopg

from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return "<h1> Welcome to Banking App </h1>"


# Tasks - 1 Create a simple flask app and run it
# Tasks 2 - connect your flask app to your postgresql database
# Tasks 3 - Create customers, accounts, transaction table using flask - models
conn = psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres", password="zxcvbnm")

print(conn)
