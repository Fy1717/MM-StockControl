class Product:
    def __init__(self, db):
        self.db = db
        self.table_name = "products"

    def create_table(self):
        try:
            query = f"CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY, name TEXT, reference TEXT, count INTEGER)"
            self.db.execute(query)
        except:
            return False

    def add(self, name, reference, count):
        try:
            countOfAllFirst = len(self.get_all())
            
            query = f"INSERT INTO {self.table_name} (name, reference, count) VALUES (?,?,?)"
            self.db.execute(query, (name, reference, count))
            
            countOfAllLast = len(self.get_all())
            
            if countOfAllFirst != countOfAllLast:
                return True
            else: 
                return False
        except:
            return False

    def get(self, id):
        try:
            query = f"SELECT name, reference, count FROM {self.table_name} WHERE id=?"
            
            return self.db.fetchall(query, (id,))
        except:
            return False

    def get_all(self):
        try:
            query = f"SELECT id, name, reference, count FROM {self.table_name}"
            
            return self.db.fetchall(query)
        except:
            return False

    def update(self, count, id):
        try:
            query = f"UPDATE {self.table_name} SET count=? WHERE id=?"
            
            self.db.execute(query, (count, id))
            
            return True
        except:
            return False

    def delete(self, id):
        try:
            countOfAllFirst = len(self.get_all())
            
            query = f"DELETE FROM {self.table_name} WHERE id=?"
            self.db.execute(query, (id,))
            
            countOfAllLast = len(self.get_all())
            
            if countOfAllFirst != countOfAllLast:
                return True
            else: 
                return False
        except:
            return False
