from ..models.to_do_tag import ToDoTag
from ..models.to_do import ToDo
from .tag_service import TagService
from .status_service import StatusService

class ToDoTagService:
    @staticmethod
    def get_by_id_to_do_and_id_tag(id_to_do,id_tag):
        to_do_tag = ToDoTag()
        to_do_tag.find_by_id_to_do_and_id_tag(id_to_do,id_tag)
        return to_do_tag
    
    @staticmethod
    def get_all_by_id_to_do(id_to_do):
        to_do_tag = ToDoTag()
        to_do_tag_list = to_do_tag.find_all_by_id_to_do(id_to_do)
        return to_do_tag_list

    @staticmethod
    def get_all_by_id_tag(id_tag):
        to_do_tag = ToDoTag()
        to_do_tag_list = to_do_tag.find_all_by_id_tag(id_tag)
        return to_do_tag_list

    @staticmethod
    def create_to_do_tag(id_to_do,id_tag):
        to_do_tag = ToDoTag(id_to_do = id_to_do,id_tag = id_tag)
        to_do_tag.insert_one()
    
    @staticmethod
    def add_tags(to_do_tags_request):
        to_do = ToDo()
        to_do.find_by_id_and_id_user(to_do_tags_request.id, to_do_tags_request.id_user)
        tag_list = ToDoTagService.treat_and_get_tag_list(to_do_tags_request, to_do)
        status = StatusService.get_by_id_and_id_user(to_do.id_status, to_do.id_user)
        return to_do, status ,tag_list

    @staticmethod
    def treat_and_get_tag_list(request, to_do):
        tag_list = []
        if len(request.tags)>0:
            for tag_request in request.tags:
                tag = TagService.get_or_create_tag(tag_request,to_do.id_user)
                tag_list.append(tag)
                ToDoTagService.create_to_do_tag(to_do.id,tag.id)
        return tag_list
    
    @staticmethod
    def remove_tag(remove_to_do_tag_request):
        to_do_tag = ToDoTagService.get_by_id_to_do_and_id_tag(remove_to_do_tag_request.id_to_do,remove_to_do_tag_request.id_tag)
        to_do_tag.delete_by_id_to_do_and_id_tag()