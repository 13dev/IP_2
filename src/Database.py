import sqlite3


class DB:
    db = ''

    def open(self, filename):
        self.db = sqlite3.connect(filename)

    def fetch_all(self, table, fields="*"):

        # Build fields string
        if isinstance(fields, list):
            fields = ', '.join(fields)

        cursor = self.db.cursor()
        cursor.execute("SELECT %s FROM `%s`" % (fields, table))

        return cursor.fetchall()

    def close(self):
        self.db.close()
        del self.db