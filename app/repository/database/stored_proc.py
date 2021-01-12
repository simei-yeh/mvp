import psycopg2
from .config import config

x = ['{"volumefactor": 1, "barlength": 300, "timeperiod": "1d", "pricefactor": 100, "data": [{"o": 15.0, "c": 14.93, "h": 15.0, "l": 14.87, "v": 191, "t": 1610116200000}], "symbol": "VEEV", "stockcode": "VEEV-1d-5min", "bar": "5min"}']

def add_stocks(stock_data):

    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()

        # call a stored procedure
        cur.execute("CALL add_stocks(%s)", stock_data)

        # commit the transaction
        conn.commit()

        # close the cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    add_stocks(x)