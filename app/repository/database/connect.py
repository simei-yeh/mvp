import os
import sys
sys.path.append(os.path.realpath('.'))

from database.config import config
import psycopg2

def fetch(query, params=None):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        configs = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**configs)

        # create a cursor
        cur = conn.cursor()

	# execute a statement
        cur.execute(query, params)

        # display the results of the query
        db_version = cur.fetchall()

        # return the results to the API
        return db_version

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert(query, params=None):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        configs = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**configs)

        # create a cursor
        cur = conn.cursor()

    	# execute a statement
        cur.execute(query, params)

        # display the results of the query
        conn.commit()
        db_version =  'row inserted'

        # return the results to the API
        return db_version

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    connect()