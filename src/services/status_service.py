from ..models.status import Status
from ..utils.to_do_exception import ToDoException
from .user_service import UserService
class StatusService:
    @staticmethod
    def get_by_id_and_id_user(id,id_user):
        status = Status()
        status.find_by_id_and_id_user(id, id_user)
        return status
    
    @staticmethod
    def get_all_by_id_user(id_user):
        status = Status()
        status_list = status.find_all_by_id_user(id_user)
        return status_list
    
    @staticmethod
    def create_status(new_status_request):
        UserService.check_user(new_status_request.id_user)
        status = Status(id_user = new_status_request.id_user,name = new_status_request.name.upper())
        status.insert_one()
        return status
    
    @staticmethod
    def update_status_name(status_request):
        status = StatusService.verify_and_get_status(status_request)
        status.update_name_by_id(status_request.name.upper())
        return status
    
    @staticmethod
    def delete_status(status_request):
        status = StatusService.verify_and_get_status(status_request)
        if status.name == status_request.name.upper():
            status.delete_by_id()
        else:
            raise ToDoException('status not found',404)

    @staticmethod
    def verify_and_get_status(status_request):
        status = Status()
        status.find_by_id_and_id_user(status_request.id,status_request.id_user)
        return status