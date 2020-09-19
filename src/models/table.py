from ..databases.to_do_database import ToDoDatabase

class Table:
    def __init__(self,id=None):
        self.id = id
        self.schema = 'to_do'
        self.database = ToDoDatabase()
    
    def execute(self, statement, values = None, operation = 'read'):
        cursor = self.database.get_cursor(operation)
        if values:
            cursor.execute(statement,values)
        else:
            cursor.execute(statement)
        return cursor
    
    def select(self, query, values = None):
        result = self.execute(query, values)
        records = list(result)
        self.database.close_connection()
        return records
    
    def insert(self, statement, values = None):
        cursor = self.execute(statement, values, 'write')
        self.database.connection.commit()
        self.id = cursor.lastrowid
        self.database.close_connection()
    
    def update(self,statement, values = None):
        self.insert(statement,values)

