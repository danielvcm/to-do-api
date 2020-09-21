from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from ..responses.status_response import StatusResponse
from ..requests.new_status_request import NewStatusRequest
from ..requests.status_request import StatusRequest
from ..controllers.status_controller import StatusController

class StatusRoute:
    router = APIRouter()

    @staticmethod
    @router.post(path="/status/new",response_model=StatusResponse)
    async def new_status(new_status_request: NewStatusRequest):
        response = await StatusController.create_status(new_status_request)
        return response
    
    @staticmethod
    @router.get('/status/{id_user}/{id}',response_model=StatusResponse)
    async def get_status_by_id_user_and_id(id_user: int, id: int):
        response = await StatusController.get_status_by_id_and_id_user(id,id_user)
        return response
    
    @staticmethod
    @router.get('/status/{id_user}',response_model=List[StatusResponse])
    async def get_all_status_by_id_user(id_user: int):
        response = await StatusController.get_all_by_id_user(id_user)
        return response
    
    @staticmethod
    @router.put('/status',response_model=StatusResponse)
    async def update_status_name(status_request: StatusRequest):
        response = await StatusController.update_status_name(status_request)
        return response

    @staticmethod
    @router.delete('/status',)
    async def delete_status_name(status_request: StatusRequest):
        response = await StatusController.delete_status(status_request)
        return JSONResponse(content= response,status_code=200)