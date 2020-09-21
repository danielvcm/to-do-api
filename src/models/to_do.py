from .table import Table
from ..utils.to_do_exception import ToDoException
class ToDo(Table):
    def __init__(self,id=None,id_user=None,id_status=None,name=None,
                description=None,due_date=None):
        self.id_user = id_user
        self.id_status = id_status
        self.name = name
        self.description = description
        self.due_date = due_date
        self.table = 'to_dos'
        super().__init__(id)
    
    def insert_one(self):
        statement = f"""INSERT INTO `to_do`.`to_dos`
                    (`id_user`,
                    `id_status`,
                    `name`,
                    `description`,
                    `due_date`)
                    VALUES
                    ({self.id_user},
                    {self.id_status},
                    '{self.name}',%s,%s);
                    """
        self.insert(statement,(self.description,self.due_date))
    
    def find_by_id_and_id_user(self,id,id_user):
        self.id = id
        self.id_user = id_user
        query = f"""
                SELECT * FROM `{self.schema}`.`{self.table}`
                WHERE id = {self.id} AND id_user = {self.id_user}
                """
        self.find_one(query)

    def find_one(self, query):
        result = self.select(query)
        if len(result)>0:
            self.id = result[0]['id']
            self.id_user = result[0]['id_user']
            self.id_status = result[0]['id_status']
            self.name = result[0]['name']
            self.description = result[0]['description']
            self.due_date = result[0]['due_date']
        else:
            raise ToDoException('to do not found',404)

    def find_all_by_id_user(self,id_user):
        query = f"""
                SELECT * FROM `{self.schema}`.`{self.table}`
                WHERE id_user = {id_user}
                """
        to_do_list = self.find_many(query)
        return to_do_list

    def find_all_by_id_user_and_id_status(self,id_user,id_status):
        query = f"""
                SELECT * FROM `{self.schema}`.`{self.table}`
                WHERE id_user = {id_user} AND id_status = {id_status}
                """
        to_do_list = self.find_many(query)
        return to_do_list

    def find_many(self, query):
        result = self.select(query)
        to_do_list = [ToDo(to_do['id'],to_do['id_user'],to_do['id_status'],to_do['name'],to_do['description'],to_do['due_date']) for to_do in result]
        if len(to_do_list) == 0:
            raise ToDoException("wasn't able to find any tag related to this user",404)
        return to_do_list
    
    def update_name_by_id(self,name,id=None):
        self.verify_id_parameter(id)
        self.name = name
        statement = f"""UPDATE `{self.schema}`.`{self.table}`
                        SET name = '{self.name}'
                        WHERE id = {self.id}
                    """
        self.update(statement)
    
    def update_id_status_by_id(self,id_status,id=None):
        self.verify_id_parameter(id)
        self.id_status = id_status
        statement = f"""UPDATE `{self.schema}`.`{self.table}`
                        SET id_status = {self.id_status}
                        WHERE id = {self.id}
                    """
        self.update(statement)

    def update_description_by_id(self,description,id=None):
        self.verify_id_parameter(id)
        self.description = description
        statement = f"""UPDATE `{self.schema}`.`{self.table}`
                        SET description = '{self.description}'
                        WHERE id = {self.id}
                    """
        self.update(statement)
    
    def update_due_date_by_id(self,due_date,id=None):
        self.verify_id_parameter(id)
        self.due_date = due_date
        statement = f"""UPDATE `{self.schema}`.`{self.table}`
                        SET due_date = %s
                        WHERE id = {self.id}
                    """
        self.update(statement,self.due_date)
    
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
            "id_status": self.id_status,
            "name": self.name,
            "description": self.description,
            "due_date": self.due_date,
        }