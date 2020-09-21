from ..controllers.to_do_controller import ToDoController
from ..responses.to_do_response import ToDoResponse
from ..requests.new_to_do_request import NewToDoRequest
from ..requests.update_status_to_do_request import UpdateStatusToDoRequest
from ..requests.update_name_to_do_request import UpdateNameToDoRequest
from ..requests.update_description_to_do_request import UpdateDescriptionToDoRequest
from ..requests.update_due_date_to_do_request import UpdateDueDateToDoRequest
from ..requests.to_do_tags_request import ToDoTagsRequest
from ..requests.remove_to_do_tag_request import RemoveToDoTagRequest
from ..requests.delete_to_do_request import DeleteToDoRequest
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
class ToDoRoute:
    router = APIRouter()

    @staticmethod
    @router.post(path="/to-do/new",response_model=ToDoResponse)
    async def new_to_do(new_to_do_request: NewToDoRequest):
        response = await ToDoController.create_to_do(new_to_do_request)
        return response
    
    @staticmethod
    @router.get(path="/to-do/{id_user}/{id}",response_model=ToDoResponse)
    async def get_by_id_user_and_id(id_user:int, id:int):
        response = await ToDoController.get_by_id_and_id_user(id,id_user)
        return response

    @staticmethod
    @router.get(path="/to-do/{id_user}",response_model=List[ToDoResponse])
    async def get_all_by_id_user(id_user:int):
        response = await ToDoController.get_all_by_id_user(id_user)
        return response
    
    @staticmethod
    @router.get(path="/to-do/{id_user}/status/{id_status}",response_model=List[ToDoResponse])
    async def get_all_by_id_user_and_id_status(id_user: int, id_status: int):
        response = await ToDoController.get_all_by_id_user_and_id_status(id_user, id_status)
        return response

    @staticmethod
    @router.get(path="/to-do/{id_user}/tag/{id_tag}",response_model=List[ToDoResponse])
    async def get_all_by_id_user_and_id_tag(id_user: int, id_tag: int):
        response = await ToDoController.get_all_by_id_user_and_id_tag(id_user, id_tag)
        return response

    @staticmethod
    @router.put(path="/to-do/new-status",response_model=ToDoResponse)
    async def update_to_do_status(update_status_to_do_request: UpdateStatusToDoRequest):
        response = await ToDoController.update_to_do_status(update_status_to_do_request)
        return response
    
    @staticmethod
    @router.put(path="/to-do/new-name",response_model=ToDoResponse)
    async def update_to_do_name(update_name_to_do_request: UpdateNameToDoRequest):
        response = await ToDoController.update_to_do_name(update_name_to_do_request)
        return response
    
    @staticmethod
    @router.put(path="/to-do/new-description",response_model=ToDoResponse)
    async def update_to_do_description(update_description_to_do_request: UpdateDescriptionToDoRequest):
        response = await ToDoController.update_to_do_description(update_description_to_do_request)
        return response
    
    @staticmethod
    @router.put(path="/to-do/new-due_date",response_model=ToDoResponse)
    async def update_to_do_due_date(update_due_date_to_do_request: UpdateDueDateToDoRequest):
        response = await ToDoController.update_to_do_due_date(update_due_date_to_do_request)
        return response
    
    @staticmethod
    @router.put(path="/to-do/add-tags",response_model=ToDoResponse)
    async def add_tags_to_to_do(to_do_tags_request: ToDoTagsRequest):
        response = await ToDoController.add_tags(to_do_tags_request)
        return response

    @staticmethod
    @router.put(path="/to-do/remove-tag")
    async def remove_tag_from_to_do(remove_to_do_tag_request: RemoveToDoTagRequest):
        response = await ToDoController.remove_tag(remove_to_do_tag_request)
        return JSONResponse(response, 200)
    
    @staticmethod
    @router.delete(path="/to-do")
    async def delete_to_do(delete_to_do_request: DeleteToDoRequest):
        response = await ToDoController.delete_to_do(delete_to_do_request)
        return JSONResponse(response, 200) 