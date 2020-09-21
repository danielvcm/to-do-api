from ..services.status_service import StatusService
from ..responses.status_response import StatusResponse
class StatusController:
    @staticmethod
    async def get_status_by_id_and_id_user(id,id_user):
        status = StatusService.get_by_id_and_id_user(id,id_user)
        response = StatusResponse.parse_obj(status.to_dict())
        return response
    
    @staticmethod
    async def get_all_by_id_user(id_user):
        status_list = StatusService.get_all_by_id_user(id_user)
        response = [StatusResponse.parse_obj(status.to_dict()) for status in status_list]
        return response
    
    @staticmethod
    async def create_status(new_status_request):
        status = StatusService.create_status(new_status_request)
        response = StatusResponse.parse_obj(status.to_dict())
        return response
    
    @staticmethod
    async def update_status_name(status_request):
        status = StatusService.update_status_name(status_request)
        response = StatusResponse.parse_obj(status.to_dict())
        return response
    
    @staticmethod
    async def delete_status(status_request):
        StatusService.delete_status(status_request)
        return {"message": 'Status deleted'}