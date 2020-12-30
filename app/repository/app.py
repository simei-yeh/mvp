import flask
from flask import request, jsonify
from .connect import connect
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# update static route
@app.route('/api', methods=['GET'])
def home():
    query1 = "select sum(b.weighted_score) as total_w_score, sum(b.num_comments) as tot_comments, sum(b.score) as tot_score, b.ticker from vol.wsb b where to_timestamp(b.   created) > (current_timestamp - interval '1 day') group by b.ticker"
    results=connect(query1,"fetch")
    return jsonify(results)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# retrieve information for a specific crypto
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

    results = connect(query, "fetch", to_filter)
    print(results)

    return jsonify(results)

if __name__ == "__main__":
    app.run()