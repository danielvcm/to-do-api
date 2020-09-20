from .table import Table
from ..utils.to_do_exception import ToDoException
import pymysql
class User(Table):
    def __init__(self,id=None,name=None,user_name=None,password=None):
        self.name = name
        self.user_name = user_name
        self.password = password
        self.table = 'users'
        super().__init__(id)
    
    def insert_one(self):
        statement = f"""INSERT INTO `{self.schema}`.`{self.table}`
                    (`name`,
                    `user_name`,
                    `password`)
                    VALUES
                    ("{self.name}",
                    "{self.user_name}",
                    "{self.password}");
                    """
        try:
            self.insert(statement)
        except pymysql.err.IntegrityError:
            raise ToDoException('User name already in use',400)
    
    def find_by_id(self,id):
        
        self.id = id
        query = f"""
                SELECT * FROM `{self.schema}`.`{self.table}`
                WHERE id = {self.id}
                """
        self.find(query)
    
    def find_by_user_name(self,user_name):
        self.user_name = user_name
        query = f"""
                SELECT * FROM `{self.schema}`.`{self.table}`
                WHERE user_name = "{self.user_name}"
                """
        self.find(query)

    def find(self,query):
        result = self.select(query)
        if len(result) > 0:
            self.id = result[0]["id"]
            self.name = result[0]["name"]
            self.user_name = result[0]["user_name"]
            self.password = result[0]["password"]
        else:
            raise ToDoException(f"User not found",404)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_name": self.user_name,
            "password": self.password,
        }