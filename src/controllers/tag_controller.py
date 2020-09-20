from ..services.tag_service import TagService
from ..responses.tag_response import TagResponse
class TagController:
    @staticmethod
    async def get_tag_by_id_and_id_user(id,id_user):
        tag = TagService.get_by_id_and_id_user(id,id_user)
        response = TagResponse.parse_obj(tag.to_dict())
        return response
    
    @staticmethod
    async def get_all_by_id_user(id_user):
        tag_list = TagService.get_all_by_id_user(id_user)
        response = [TagResponse.parse_obj(tag.to_dict()) for tag in tag_list]
        return response
    
    @staticmethod
    async def create_tag(new_tag_request):
        tag = TagService.create_tag(new_tag_request)
        response = TagResponse.parse_obj(tag.to_dict())
        return response
    
    @staticmethod
    async def update_tag_name(tag_request):
        tag = TagService.update_tag_name(tag_request)
        response = TagResponse.parse_obj(tag.to_dict())
        return response
    
    @staticmethod
    async def delete_tag(tag_request):
        TagService.delete_tag(tag_request)
        return {"message": 'Tag deleted'}