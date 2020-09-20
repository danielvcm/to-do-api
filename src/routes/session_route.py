from fastapi import APIRouter
from ..controllers.session_controller import SessionController
from ..requests.new_user_request import NewUserRequest
from ..requests.login_request import LoginRequest
from ..responses.user_response import UserResponse
class SessionRoute:
    router = APIRouter()

    @staticmethod
    @router.post(path="/session/new_user",response_model=UserResponse)
    async def new_user(new_user_request: NewUserRequest):
        response = await SessionController.create_user(new_user_request)
        return response

    @staticmethod
    @router.post(path="/session/login",response_model=UserResponse)
    async def login(login_request: LoginRequest):
        response = await SessionController.login(login_request)
        return response

    