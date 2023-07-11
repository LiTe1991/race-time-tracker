import configparser

from pysqlcipher3 import dbapi2 as sqlite3
from pathlib import Path


class DBAccess:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("Config.ini")

        self.conn = None
        self.cursor = None
        self.dbname = config["DBSettings"]["DBName"]
        self.dbPassword = config["DBSettings"]["DBPassword"]

    def conn_db(self):
        if not self.db_file_exists():
            raise ValueError('DB wurde nicht initialisiert')

        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"PRAGMA key='{self.dbPassword}'")

    def db_file_exists(self):
        path = Path(self.dbname)
        return path.exists() and path.is_file()

    def get_all_drivers(self):
        self.conn_db()

        res = self.cursor.execute(
            '''
            SELECT * FROM Driver
            '''
        )

        return res.fetchall()
