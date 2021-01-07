import flask
from flask import request, jsonify
from .connect import connect
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# update static route
@app.route('/api', methods=['GET'])
def home():
    query1 = "SELECT SUM(b.weighted_score) as total_w_score, SUM(b.num_comments) as tot_comments, SUM(b.score) as tot_score, b.ticker, count(b.name) FROM vol.wsb b WHERE to_timestamp(b.   created) > (current_timestamp - interval '1 day') GROUP BY b.ticker order by total_w_score desc"
    results=connect(query1,"fetch")
    query2 = "SELECT * FROM vol.stocks WHERE stockcode = 'TSLA-2w-30min'"
    results2=connect(query2, "fetch")
    query3 = "SELECT * FROM (SELECT DISTINCT ON (c.asset_id_quote) c.time,c.asset_id_quote,c.rate FROM vol.crypto c WHERE c.asset_id_quote in ('BTC','ETH','BCH','LTC','EOS','DASH')  ORDER BY c.asset_id_quote, c.time desc) as a ORDER BY a.rate desc"
    results3=connect(query3, "fetch")
    return jsonify(results, results2, results3)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# retrieve information for a specific crypto
@app.route('/api/v1/quotes/crypto', methods=['GET'])
def api_crypto():
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

# retrieve information for a specific stock ticker
@app.route('/api/v1/quotes/stocks', methods=['GET'])
def api_stocks():
    query_parameters = request.args

    ticker = query_parameters.get('ticker')
    interval = query_parameters.get('interval')

    query = "SELECT * FROM vol.stocks WHERE"
    to_filter = []

    if ticker:
        query += ' symbol=(%s) AND'
        to_filter.append(ticker)
    if interval:
        query += ' bar=(%s)'
        to_filter.append(interval)
    if not (ticker or interval):
        return page_not_found(404)

    results = connect(query, "fetch", to_filter)
    print(results)

    if not results:
        print('could not find')
        return page_not_found(404)
    else:
        return jsonify(results)

@app.route('/api/v1/autosuggest', methods=['GET'])
def autosuggest():
    query_parameters = request.args

    autosuggest = query_parameters.get('ticker')

    query = "SELECT DISTINCT(symbol) FROM vol.stocks WHERE symbol LIKE %s ORDER BY symbol ASC"
    to_filter = []

    if autosuggest:
        modAutosuggest = '{}%'.format(autosuggest)
        to_filter.append(modAutosuggest)
    else:
        return page_not_found(404)

    results = connect(query, "fetch", to_filter)
    print(results)

    if not results:
        print('could not find')
        return page_not_found(404)
    else:
        res = []
        for l in results:
            res.append(l[0])
        return jsonify(res)

if __name__ == "__main__":
    app.run()