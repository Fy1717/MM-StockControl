import sqlite3

class Database:
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except:
            return False

    def execute(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
                
            self.conn.commit()
            
            return True
        except:
            return False

    def fetchall(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
                
            return self.cursor.fetchall()
        except:
            return False

    def __del__(self):
        try:
            self.conn.close()
        except:
            return False