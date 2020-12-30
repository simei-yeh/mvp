import flask
from flask import request, jsonify
from .connect import connect
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# update static route
@app.route('/api', methods=['GET'])
def home():
    query1 = "SELECT SUM(b.weighted_score) as total_w_score, SUM(b.num_comments) as tot_comments, SUM(b.score) as tot_score, b.ticker FROM vol.wsb b WHERE to_timestamp(b.   created) > (current_timestamp - interval '1 day') GROUP BY b.ticker"
    results=connect(query1,"fetch")
    query2 = "SELECT * FROM vol.stocks WHERE stockcode = 'TSLA-1m-1800'"
    results2=connect(query2, "fetch")
    query3 = "SELECT DISTINCT ON (c.asset_id_quote) c.time,c.asset_id_quote,c.rate FROM vol.crypto c WHERE c.asset_id_quote in ('BTC','ETH','BCH','LTC','EOS','DASH','OXT')  ORDER BY c.asset_id_quote, c.time desc"
    results3=connect(query3, "fetch")
    return jsonify(results, results2, results3)


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