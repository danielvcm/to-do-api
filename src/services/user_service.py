from ..models.user import User
from ..utils.to_do_exception import ToDoException
from .encryption_service import EncriptionService

class UserService:
    
    @staticmethod
    def create_user(new_user_request):
        new_user = User(name=new_user_request.name,user_name=new_user_request.user_name)
        EncriptionService.encrypt_password(new_user_request, new_user)
        new_user.insert_one()
        return new_user

    @staticmethod
    def login(login_request):
        user = User()
        user.find_by_user_name(user_name=login_request.user_name)
        real_password = EncriptionService.decrypt_password(user)
        if real_password == login_request.password:
            return user
        raise ToDoException('Incorrect password',400)
    
    @staticmethod
    def check_user(id):
        user = User()
        user.find_by_id(id)
        