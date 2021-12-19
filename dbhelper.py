import sqlite3


class DBHelper:
    def __init__(self, dbname="PKOB.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

