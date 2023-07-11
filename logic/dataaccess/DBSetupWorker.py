import time, configparser

from pysqlcipher3 import dbapi2 as sqlite3
from pathlib import Path
from PySide6.QtCore import QRunnable, Slot, Signal, QObject


class DBSetupWorkerSignal(QObject):
    finished = Signal(object)
    progress = Signal(int, int)


class DBSetupWorker(QRunnable):

    def __init__(self, fn: object):
        super(DBSetupWorker, self).__init__()
        self.fn = fn
        self.signals = DBSetupWorkerSignal()

        config = configparser.ConfigParser()
        config.read("Config.ini")

        self.conn = None
        self.cursor = None
        self.dbname = config["DBSettings"]["DBName"]
        self.dbPassword = config["DBSettings"]["DBPassword"]
        self.dbCreationSteps = 8

    def conn_db(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"PRAGMA key='{self.dbPassword}'")

    def create_db(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Driver (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            guest BIT NOT NULL);
            '''
        )
        self.signals.progress.emit(1, self.dbCreationSteps)

        time.sleep(1)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS RaceType (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
            );
            '''
        )
        self.signals.progress.emit(2, self.dbCreationSteps)

        time.sleep(1)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS RaceConfiguration (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            raceTypeId INTEGER NOT NULL,
            value1 TEXT NULL,
            FOREIGN KEY(raceTypeId) REFERENCES RaceType(id)
            );
            '''
        )
        self.signals.progress.emit(3, self.dbCreationSteps)

        time.sleep(1)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Race (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            raceTypeId INTEGER NOT NULL,
            active BIT NOT NULL,
            raceDate DATETIME NOT NULL,
            FOREIGN KEY(raceTypeId) REFERENCES RaceType(id)
            );
            '''
        )
        self.signals.progress.emit(4, self.dbCreationSteps)

        time.sleep(1)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Run (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            raceId INTEGER NOT NULL,
            FOREIGN KEY(raceId) REFERENCES Race(id)
            );
            '''
        )
        self.signals.progress.emit(5, self.dbCreationSteps)

        time.sleep(1)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Measure (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            driverId INTEGER NOT NULL,
            runId INTEGER NOT NULL,
            time TIME NOT NULL,
            points INTEGER NULL,
            FOREIGN KEY(driverId) REFERENCES Driver(id),
            FOREIGN KEY(runId) REFERENCES Run(id)
            );
            '''
        )
        self.signals.progress.emit(6, self.dbCreationSteps)

        time.sleep(1)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS ConfigurationIdentifier (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            identifier TEXT NOT NULL,
            description TEXT NULL);
            '''
        )
        self.signals.progress.emit(7, self.dbCreationSteps)

        time.sleep(1)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS ConfigurationItem (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            identifierId INTEGER NOT NULL,
            value TEXT NOT NULL,
            FOREIGN KEY(identifierId) REFERENCES ConfigurationIdentifier(id)
            );
            '''
        )
        self.signals.progress.emit(8, self.dbCreationSteps)

        time.sleep(1)

        self.conn.commit()
        self.conn.close()

    def db_file_exists(self):
        path = Path(self.dbname)
        return path.exists() and path.is_file()

    @Slot()
    def run(self):
        if self.db_file_exists():
            self.signals.finished.emit("DB already exists")
            return

        self.conn_db()
        self.create_db()
        self.signals.finished.emit("DB created")
