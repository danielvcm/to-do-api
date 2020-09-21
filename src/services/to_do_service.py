from ..models.to_do import ToDo
from ..utils.to_do_exception import ToDoException
from .status_service import StatusService
from .tag_service import TagService
from .to_do_tag_service import ToDoTagService
from .user_service import UserService

class ToDoService:
    @staticmethod
    def get_by_id_and_id_user(id,id_user):
        to_do = ToDo()
        to_do.find_by_id_and_id_user(id, id_user)
        status, tag_list = ToDoService.get_status_and_tags(to_do.id,to_do.id_status ,id_user)
        return to_do, status, tag_list

    @staticmethod
    def get_status_and_tags(id,id_status, id_user):
        status = StatusService.get_by_id_and_id_user(id_status,id_user)
        tag_list = ToDoService.get_tag_list(id, id_user)
        return status, tag_list

    @staticmethod
    def get_tag_list(id, id_user):
        id_tag_list = ToDoTagService.get_all_by_id_to_do(id)
        tag_list = []
        for tag_to_do in id_tag_list:
            tag = TagService.get_by_id_and_id_user(tag_to_do.id_tag,id_user)
            tag_list.append(tag)
        return tag_list
    
    @staticmethod
    def get_all_by_id_user(id_user):
        to_do = ToDo()
        to_do_list = to_do.find_all_by_id_user(id_user)
        status_to_do_list, tag_to_do_list = ToDoService.get_satus_and_tag_lists(to_do_list, id_user)
        return to_do_list, status_to_do_list, tag_to_do_list

    @staticmethod
    def get_satus_and_tag_lists(to_do_list, id_user):
        tag_to_do_list = []
        status_to_do_list = []
        for to_do_item in to_do_list:
            status, tag_list = ToDoService.get_status_and_tags(to_do_item.id,to_do_item.id_status ,id_user)
            status_to_do_list.append(status)
            tag_to_do_list.append(tag_list)
        return status_to_do_list, tag_to_do_list
    
    @staticmethod
    def get_all_by_id_user_and_id_status(id_user,id_status):
        to_do = ToDo()
        to_do_list = to_do.find_all_by_id_user_and_id_status(id_user,id_status)
        status_to_do_list, tag_to_do_list = ToDoService.get_satus_and_tag_lists(to_do_list, id_user)
        return to_do_list, status_to_do_list, tag_to_do_list
    
    @staticmethod
    def get_all_by_id_user_and_id_tag(id_user,id_tag):
        to_do_tag_list = ToDoTagService.get_all_by_id_tag(id_tag)
        
        to_do_list = []
        status_to_do_list = []
        tag_to_do_list = []
        for to_do_tag in to_do_tag_list:
            to_do = ToDo()
            to_do.find_by_id_and_id_user(to_do_tag.id_to_do,id_user)
            status, tag_list = ToDoService.get_status_and_tags(to_do.id,to_do.id_status, id_user)
            to_do_list.append(to_do)
            status_to_do_list.append(status)
            tag_to_do_list.append(tag_list)
        
        return to_do_list, status_to_do_list, tag_to_do_list

    @staticmethod
    def create_to_do(new_to_do_request):
        UserService.check_user(new_to_do_request.id_user)
        status = StatusService.get_or_create_status(new_to_do_request)
        to_do = ToDo(id_user=new_to_do_request.id_user,id_status=status.id,name=new_to_do_request.name.upper(),
                    description=new_to_do_request.description,due_date=new_to_do_request.due_date)
        to_do.insert_one()
        tag_list = ToDoTagService.treat_and_get_tag_list(new_to_do_request, to_do)
        return to_do, status, tag_list

    @staticmethod
    def update_to_do_status(update_status_to_do_request):
        to_do = ToDoService.verify_and_get_to_do(update_status_to_do_request)
        status = StatusService.get_or_create_status(update_status_to_do_request)
        to_do.update_id_status_by_id(status.id)
        tag_list = ToDoService.get_tag_list(update_status_to_do_request.id, update_status_to_do_request.id_user)
        return to_do, status, tag_list

    @staticmethod
    def update_to_do_name(update_name_to_do_request):
        to_do = ToDoService.verify_and_get_to_do(update_name_to_do_request)
        to_do.update_name_by_id(update_name_to_do_request.name.upper())
        status, tag_list = ToDoService.get_status_and_tags(to_do.id, to_do.id_status, update_name_to_do_request.id_user)
        return to_do, status, tag_list
    
    @staticmethod
    def update_to_do_description(update_description_to_do_request):
        to_do = ToDoService.verify_and_get_to_do(update_description_to_do_request)
        to_do.update_description_by_id(update_description_to_do_request.description)
        status, tag_list = ToDoService.get_status_and_tags(to_do.id, to_do.id_status, update_description_to_do_request.id_user)
        return to_do, status, tag_list
    
    @staticmethod
    def update_to_do_due_date(update_due_date_to_do_request):
        to_do = ToDoService.verify_and_get_to_do(update_due_date_to_do_request)
        to_do.update_due_date_by_id(update_due_date_to_do_request.due_date)
        status, tag_list = ToDoService.get_status_and_tags(to_do.id, to_do.id_status, update_due_date_to_do_request.id_user)
        return to_do, status, tag_list

    @staticmethod
    def delete_to_do(delete_to_do_request):
        to_do = ToDoService.verify_and_get_to_do(delete_to_do_request)
        if to_do.name == delete_to_do_request.name.upper():
            to_do.delete_by_id()
        else:
            raise ToDoException("to do not found", 404)

    @staticmethod
    def verify_and_get_to_do(to_do_request):
        to_do = ToDo()
        to_do.find_by_id_and_id_user(to_do_request.id,to_do_request.id_user)
        return to_do
    