"""Main module."""
import mimetypes
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Pandas_DB_Wrangler:
    """
    Pass connect string with constructor. Connect String may be a path to a
    SQLite database or a path to a ini or text file specifying the database
    connection string. e.g.:
    postgresql+psycopg2://user:passw0rd@dns_name:5432/database_name
    """

    def __init__(self, connect_string=""):
        if connect_string != "":
            self.connect_string = self.set_connection_string(connect_string)
            self.engine = create_engine(self.connect_string)
        else:
            self.connect_string = ""
            self.engine = None

    def set_connection_string(self, url):
        path = Path(url)
        suffixes = (".db", ".gnucash", ".sqlite")
        if path.exists():
            datatype = mimetypes.guess_type(path)[0]
            if datatype == "text/plain":
                return path.read_text(encoding="utf-8").strip()
            elif datatype == "application/vnd.sqlite3" or path.suffix in suffixes:
                return f"sqlite:///{path}"
        else:
            return url

    def read_sql_file(self, filename):
        """Read SQL from File"""
        path = Path(filename)
        return path.read_text(encoding="utf-8")

    def df_fetch(self, sql, index_col=None, parse_dates=None):
        """
        Run SQL query on a database with SQL as a parameter
        Please specify connect string and db type using the
        set_connection_string function.
        """
        with self.engine.begin() as conn:
            return pd.read_sql(
                sql=text(sql), con=conn, index_col=index_col, parse_dates=parse_dates
            )
