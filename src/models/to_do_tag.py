from .table import Table
from ..utils.to_do_exception import ToDoException

class ToDoTag(Table):
    def __init__(self,id=None,id_to_do=None,id_tag=None):
        self.id_to_do = id_to_do
        self.id_tag = id_tag
        self.table = 'to_dos_tags'
        super().__init__(id)
    
    def insert_one(self):
        statement = f"""INSERT INTO `{self.schema}`.`{self.table}`
                    (`id_to_do`,
                    `id_tag`)
                    VALUES
                    ("{self.id_to_do}",
                    "{self.id_tag}");
                    """
        self.insert(statement)
    
    def find_by_id_to_do_and_id_tag(self,id_to_do,id_tag):
        self.id_to_do = id_to_do
        self.id_tag = id_tag
        query = f"""
                SELECT * FROM `{self.schema}`.`{self.table}`
                WHERE id_to_do = {self.id_to_do} AND id_tag = {self.id_tag}
                """
        self.find_one(query)
    
    def find_one(self, query):
        result = self.select(query)
        if len(result)>0:
            self.id = result[0]['id']
            self.id_to_do = result[0]['id_to_do']
            self.id_tag = result[0]['id_tag']
        else:
            raise ToDoException('to do tag relation not found',404)
    
    def find_all_by_id_to_do(self,id_to_do):
        query = f"""
                SELECT * FROM `{self.schema}`.`{self.table}`
                WHERE id_to_do = {id_to_do}
                """
        to_do_tag_list = self.find_many(query)
        return to_do_tag_list

    def find_all_by_id_tag(self,id_tag):
        query = f"""
                SELECT * FROM `{self.schema}`.`{self.table}`
                WHERE id_tag = {id_tag}
                """
        to_do_tag_list = self.find_many(query)
        return to_do_tag_list
    
    def find_many(self, query):
        result = self.select(query)
        to_do_tag_list = [ToDoTag(to_do_tag['id'],to_do_tag['id_to_do'],to_do_tag['id_tag']) for to_do_tag in result]
        return to_do_tag_list

    def delete_by_id_to_do_and_id_tag(self, id_to_do=None,id_tag=None):
        self.verify_parameters(id_to_do, id_tag)
        statement = f"""DELETE FROM `{self.schema}`.`{self.table}`
                    WHERE id_to_do = {self.id_to_do}
                    AND id_tag = {self.id_tag}
                    """
        self.delete(statement)
    
    def verify_parameters(self, id_to_do,id_tag):
        if id_to_do !=None:
            self.id_to_do = id_to_do
        if self.id_to_do == None:
            raise ToDoException("an id_to_do must be provided",400)
        if id_tag !=None:
            self.id_tag = id_tag
        if self.id_tag == None:
            raise ToDoException("an id_tag must be provided",400)