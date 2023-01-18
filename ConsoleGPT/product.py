class Product:
    def __init__(self, db):
        self.db = db
        self.table_name = "products"

    def create_table(self):
        query = f"CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY, name TEXT, reference TEXT, count INTEGER)"
        self.db.execute(query)

    def add(self, name, reference, count):
        query = f"INSERT INTO {self.table_name} (name, reference, count) VALUES (?,?,?)"
        self.db.execute(query, (name, reference, count))

    def get(self, id):
        query = f"SELECT name, reference, count FROM {self.table_name} WHERE id=?"
        return self.db.fetchall(query, (id,))

    def get_all(self):
        query = f"SELECT id, name, reference, count FROM {self.table_name}"
        return self.db.fetchall(query)

    def update(self, count, id):
        query = f"UPDATE {self.table_name} SET count=? WHERE id=?"
        self.db.execute(query, (count, id))

    def delete(self, id):
        query = f"DELETE FROM {self.table_name} WHERE id=?"
        self.db.execute(query, (id,))
