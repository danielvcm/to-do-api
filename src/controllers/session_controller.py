from ..services.user_service import UserService
from ..responses.user_response import UserResponse
class SessionController:
    @staticmethod
    async def create_user(new_user_request):
        new_user = UserService.create_user(new_user_request)
        user_response = UserResponse.parse_obj(new_user.to_dict())
        return user_response
    
    @staticmethod
    async def login(login_request):
        new_user =  UserService.login(login_request)
        user_response = UserResponse.parse_obj(new_user.to_dict())
        return user_response
