"""Main module."""
import sqlite3
import pandas as pd
import psycopg2 as pg
import pandas.io.sql as psql


class Pandas_DB_Wrangler():
    """ 
    Helper class for querying databases using pandas.
    It's essential that the CONNECT_STRING be set for
    any of the other functions to work.
    """
    def __init__(self):
        self.CONNECT_STRING = ""

    def set_connection_string(self, filename):
        """ 
        Set DB connection string from txt or ini file 
        An example of a Postgres connection might look like: 
        host='127.0.0.1' dbname=db user=user1 password='p@ssW0rD!'
        A sqlite connection is a file path, so it may look like
        '/path/to/sqlite.db'
        """ 
        with open(filename, "r") as f:
            self.CONNECT_STRING = f.readline().rstrip()
            return self.CONNECT_STRING

    def read_sql_file(self, filename):
        """ Read SQL from File """
        with open(filename, "r") as myfile:
            sql = myfile.read()
            myfile.close()
        return sql

    def fetch_from_postgres(self, sql):
        """ Run SQL query on Postgres DB given a connect string & SQL """
        cnx = pg.connect(self.CONNECT_STRING)
        df = pd.read_sql(sql, con=cnx)
        cnx.close()
        return df

    def fetch_from_sqlite(self, db_path, sql):
        """ Run SQL query on SQLite DB given a db path & SQL """
        cnx = sqlite3.connect(db_path)
        df = pd.read_sql_query(sql, con=cnx)
        cnx.close()
        return df
