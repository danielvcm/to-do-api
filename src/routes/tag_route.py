from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from ..responses.tag_response import TagResponse
from ..requests.new_tag_request import NewTagRequest
from ..requests.tag_request import TagRequest
from ..controllers.tag_controller import TagController

class TagRoute:
    router = APIRouter()

    @staticmethod
    @router.post(path="/tag/new_tag",response_model=TagResponse)
    async def new_tag(new_tag_request: NewTagRequest):
        response = await TagController.create_tag(new_tag_request)
        return response
    
    @staticmethod
    @router.get('/tag/{id_user}/{id}',response_model=TagResponse)
    async def get_tag_by_id_user_and_id(id_user: int, id: int):
        response = await TagController.get_tag_by_id_and_id_user(id,id_user)
        return response
    
    @staticmethod
    @router.get('/tag/{id_user}',response_model=List[TagResponse])
    async def get_all_tag_by_id_user(id_user: int):
        response = await TagController.get_all_by_id_user(id_user)
        return response
    
    @staticmethod
    @router.put('/tag',response_model=TagResponse)
    async def update_tag_name(tag_request: TagRequest):
        response = await TagController.update_tag_name(tag_request)
        return response

    @staticmethod
    @router.delete('/tag',)
    async def delete_tag_name(tag_request: TagRequest):
        response = await TagController.delete_tag(tag_request)
        return JSONResponse(content= response,status_code=200)