import flask
from flask import request, jsonify
from connect import connect
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    query = 'SELECT * from vol.crypto'
    connect(query)
    return '''<h1>Distant Reading Archive</h1> <p>A prototype API for distant reading of science fiction novels.</p>'''


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/quotes/crypto', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    crypto = query_parameters.get('crypto')

    query = "SELECT * FROM vol.crypto WHERE"
    to_filter = []

    if id:
        query += ' id=(%s) AND'
        to_filter.append(id)
    if crypto:
        query += ' asset_id_quote=(%s) AND'
        to_filter.append(crypto)
    if not (id or crypto):
        return page_not_found(404)

    # strip the last AND from the query
    query = query[:-4]

    results = connect(query, to_filter)
    print(results)

    return jsonify(results)

app.run()