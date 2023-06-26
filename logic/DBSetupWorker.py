from pysqlcipher3 import dbapi2 as sqlite3

from PySide6.QtCore import QRunnable, Slot, Signal, QObject


class DBSetupWorkerSignal(QObject):
    finished = Signal(object)
    progress = Signal(int)


class DBSetupWorker(QRunnable):

    def __init__(self, fn: object):
        super(DBSetupWorker, self).__init__()
        self.fn = fn
        self.signals = DBSetupWorkerSignal()

        self.dbname = "race_tracker.db"

    def conn_db(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA key='mypassword'")

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
        self.signals.progress.emit(1)

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS ConfigurationIdentifier (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            identifier TEXT NOT NULL,
            description TEXT NULL);
            '''
        )
        self.signals.progress.emit(2)

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
        self.signals.progress.emit(3)

        self.conn.commit()
        self.conn.close()

    @Slot()
    def run(self):
        self.conn_db()
        self.create_db()
        self.signals.finished.emit("OK")
