import pymysql
from ..utils.to_do_exception import ToDoException
import os

class ToDoDatabase:
    def __init__(self):
        self.connection = None
    
    def connect(self,operation='read'):
        if operation == 'write':
            self.connection = pymysql.connect(
                host=os.getenv('DB_HOST'),
                port=int(os.getenv('DB_PORT')),
                user=os.getenv('DB_USER'),
                passwd=os.getenv('DB_PASSWORD'),
                charset='utf8',
                cursorclass=pymysql.cursors.Cursor
            )
        elif operation == 'read':
            self.connection = pymysql.connect(
                host=os.getenv('DB_HOST'),
                port=int(os.getenv('DB_PORT')),
                user=os.getenv('DB_USER'),
                passwd=os.getenv('DB_PASSWORD'),
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
        else:
            raise ToDoException("A connection operation must be 'read' or 'write'",500)
    
    def close_connection(self):
        if self.connection != None and self.connection.open:
            self.connection.close()


