from ..models.tag import Tag
from ..utils.to_do_exception import ToDoException
from .user_service import UserService
class TagService:
    @staticmethod
    def get_by_id_and_id_user(id,id_user):
        tag = Tag()
        tag.find_by_id_and_id_user(id, id_user)
        return tag
    
    @staticmethod
    def get_all_by_id_user(id_user):
        tag = Tag()
        tag_list = tag.find_all_by_id_user(id_user)
        return tag_list
    
    @staticmethod
    def create_tag(new_tag_request):
        UserService.check_user(new_tag_request.id_user)
        tag = Tag(id_user = new_tag_request.id_user,name = new_tag_request.name.upper())
        tag.insert_one()
        return tag
    
    @staticmethod
    def update_tag_name(tag_request):
        tag = TagService.verify_and_get_tag(tag_request)
        tag.update_name_by_id(tag_request.name.upper())
        return tag
    
    @staticmethod
    def delete_tag(tag_request):
        tag = TagService.verify_and_get_tag(tag_request)
        if tag.name == tag_request.name.upper():
            tag.delete_by_id()
        else:
            raise ToDoException("tag not found", 404)

    @staticmethod
    def verify_and_get_tag(tag_request):
        tag = Tag()
        tag.find_by_id_and_id_user(tag_request.id,tag_request.id_user)
        return tag
    
    @staticmethod
    def get_or_create_tag(request,id_user):
        try:
            tag = Tag()
            tag.find_by_name_and_id_user(request.upper(),id_user)
        except ToDoException:
            tag = Tag(id_user = id_user,name=request.upper())
            tag.insert_one()
        return tag