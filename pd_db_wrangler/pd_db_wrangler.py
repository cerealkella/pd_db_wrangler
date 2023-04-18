"""Main module."""
import mimetypes
from pathlib import Path

import pandas as pd
import tomli
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
        self.options = {}
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

    def pandas_toml_extractor(self, sql: str) -> str:
        """
        Looks for comments in a SQL file to help pandas determine types.
        Example SQL comment:
        /*pandas*
        [parse_date]
        parse_dates = []
        index_col = ["created_at"]
        [dtype]
        user_name = "string"
        user_id = "int64"
        created_at = "datetime64[ns, UTC]"
        [timezone]
        tz = "America/Chicago"
        *pandas*/

        Args:
            sql (str): SQL to parse

        Returns:
            str: string containing only the TOML to parse
        """
        toml_text = sql[
            sql.find(start := "/*pandas*") + len(start) : sql.find("*pandas*/")
        ]
        try:
            toml_dict = tomli.loads(toml_text)
        except tomli.TOMLDecodeError:
            print("No valid toml found in SQL")
        return toml_dict

    def read_sql_file(self, filename):
        """Read SQL from File"""
        path = Path(filename)
        sql = path.read_text(encoding="utf-8")
        self.options = self.pandas_toml_extractor(sql)
        return sql

    def df_fetch(
        self,
        sql,
        index_col=None,
        parse_dates=None,
        dtype=None,
    ):
        """
        Run SQL query on a database with SQL as a parameter
        Please specify connect string and db type using the
        set_connection_string function.
        """
        options = ("parse_dates", "dtype", "index_col")

        local_args = print(locals().keys())
        for option in options:
            try:
                if parse_dates is None:
                    parse_dates = self.options["parse_dates"]
                if dtype is None:
                    dtype = self.options("dtype")
                if index_col is None:
                    index_col = self.options("index_col")
            except KeyError:
                pass

        with self.engine.begin() as conn:
            return pd.read_sql(
                sql=text(sql),
                con=conn,
                index_col=index_col,
                parse_dates=parse_dates,
                dtype=dtype,
            )


pdw = Pandas_DB_Wrangler()
sql = pdw.read_sql_file("pd_db_wrangler/test_query.sql")
print(sql)
print(pdw.options)

parse_dates = pdw.options["parse_date"]
dtype = pdw.options["dtype"]
print(dtype)
