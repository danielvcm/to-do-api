from ..models.user import User
from ..utils.to_do_exception import ToDoException
from .encryption_service import EncriptionService

class UserService:
    
    @staticmethod
    def create_user(user_request):
        new_user = User(name=user_request.name,user_name=user_request.user_name)
        EncriptionService.encrypt_password(user_request, new_user)
        new_user.insert_one()

    @staticmethod
    def login(user_request):
        user = User()
        user.find_by_user_name(user_name=user_request.user_name)
        real_password = EncriptionService.decrypt_password(user)
        if real_password == user_request.password:
            return user
        raise ToDoException('Incorrect password',400)

        