from .table import Table
from ..utils.to_do_exception import ToDoException
class Tag(Table):
    def __init__(self,id=None,id_user=None,name=None):
        self.id_user = id_user
        self.name = name
        self.table = 'tags'
        super().__init__(id)
    
    def insert_one(self):
        statement = f"""INSERT INTO `{self.schema}`.`{self.table}`
                    (`name`,
                    `id_user`)
                    VALUES
                    ("{self.name}",
                    "{self.id_user}");
                    """
        self.insert(statement)
    
    def find_by_id_and_id_user(self,id,id_user):
        self.id = id
        self.id_user = id_user
        query = f"""
                SELECT * FROM `{self.schema}`.`{self.table}`
                WHERE id = {self.id} AND id_user = {self.id_user}
                """
        self.find_one(query)
    
    def find_by_name_and_id_user(self,name,id_user):
        self.name = name
        self.id_user = id_user

        query = f"""
                SELECT * FROM `{self.schema}`.`{self.table}`
                WHERE name = '{self.name}' AND id_user = {self.id_user}
                """
        self.find_one(query)
    
    def find_one(self, query):
        result = self.select(query)
        if len(result)>0:
            self.id = result[0]['id']
            self.id_user = result[0]['id_user']
            self.name = result[0]['name']
        else:
            raise ToDoException('tag not found',404)
    
    def find_all_by_id_user(self,id_user):
        query = f"""
                SELECT * FROM `{self.schema}`.`{self.table}`
                WHERE id_user = {id_user}
                """
        result = self.select(query)
        tag_list = [Tag(tag['id'],tag['id_user'],tag['name']) for tag in result]
        if len(tag_list) == 0:
            raise ToDoException("wasn't able to find any tag related to this user",404)
        return tag_list
    
    def update_name_by_id(self,name,id=None):
        self.verify_id_parameter(id)
        self.name = name
        statement = f"""UPDATE `{self.schema}`.`{self.table}`
                        SET name = '{self.name}'
                        WHERE id = {self.id}
                    """
        self.update(statement)

    def delete_by_id(self, id=None):
        self.verify_id_parameter(id)
        statement = f"""DELETE FROM `{self.schema}`.`{self.table}`
                    WHERE id = {self.id}
                    """
        self.delete(statement)
    
    def verify_id_parameter(self, id):
        if id !=None:
            self.id = id
        if self.id == None:
            raise ToDoException("an id must be provided",400)
    
    def to_dict(self):
        return{
            "id": self.id,
            "id_user": self.id_user,
            "name": self.name
        }