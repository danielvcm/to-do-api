from ..services.to_do_service import ToDoService
from ..services.to_do_tag_service import ToDoTagService
from ..responses.to_do_response import ToDoResponse
class ToDoController:
    @staticmethod
    async def get_by_id_and_id_user(id,id_user):
        to_do, status, tag_list = ToDoService.get_by_id_and_id_user(id,id_user)
        response = ToDoController.build_to_do_response(to_do, status, tag_list)
        return response

    @staticmethod
    async def get_all_by_id_user(id_user):
        to_do_list, status_to_do_list, tag_to_do_list = ToDoService.get_all_by_id_user(id_user)
        response = ToDoController.parse_lists_and_build_response(to_do_list, status_to_do_list, tag_to_do_list)
        return response
 
    @staticmethod
    async def get_all_by_id_user_and_id_status(id_user,id_status):
        to_do_list, status_to_do_list, tag_to_do_list = ToDoService.get_all_by_id_user_and_id_status(id_user,id_status)
        response = ToDoController.parse_lists_and_build_response(to_do_list, status_to_do_list, tag_to_do_list)
        return response
    
    @staticmethod
    async def get_all_by_id_user_and_id_tag(id_user,id_tag):
        to_do_list, status_to_do_list, tag_to_do_list = ToDoService.get_all_by_id_user_and_id_tag(id_user,id_tag)
        response = ToDoController.parse_lists_and_build_response(to_do_list, status_to_do_list, tag_to_do_list)
        return response

    @staticmethod
    async def create_to_do(new_to_do_request):
        to_do, status, tag_list = ToDoService.create_to_do(new_to_do_request)
        response = ToDoController.build_to_do_response(to_do, status, tag_list)
        return response

    @staticmethod
    async def update_to_do_status(update_status_to_do_request):
        to_do, status, tag_list = ToDoService.update_to_do_status(update_status_to_do_request)
        response = ToDoController.build_to_do_response(to_do, status, tag_list)
        return response
    
    @staticmethod
    async def update_to_do_name(update_name_to_do_request):
        to_do, status, tag_list = ToDoService.update_to_do_name(update_name_to_do_request)
        response = ToDoController.build_to_do_response(to_do, status, tag_list)
        return response

    @staticmethod
    async def update_to_do_description(update_description_to_do_request):
        to_do, status, tag_list = ToDoService.update_to_do_description(update_description_to_do_request)
        response = ToDoController.build_to_do_response(to_do, status, tag_list)
        return response
    
    @staticmethod
    async def update_to_do_due_date(update_due_date_to_do_request):
        to_do, status, tag_list = ToDoService.update_to_do_due_date(update_due_date_to_do_request)
        response = ToDoController.build_to_do_response(to_do, status, tag_list)
        return response

    @staticmethod
    async def add_tags(to_do_tags_request):
        to_do, status ,tag_list = ToDoTagService.add_tags(to_do_tags_request)
        response = ToDoController.build_to_do_response(to_do, status, tag_list)
        return response
    
    @staticmethod
    async def remove_tag(remove_to_do_tag_request):
        ToDoTagService.remove_tag(remove_to_do_tag_request)
        return {'message': "tag removed from to do"}
    
    @staticmethod
    async def delete_to_do(delete_to_do_request):
        ToDoService.delete_to_do(delete_to_do_request)
        return {'message': "to do deleted"}
    
    @staticmethod
    def parse_lists_and_build_response(to_do_list, status_to_do_list, tag_to_do_list):
        response = []
        for i in range(len(to_do_list)):
            to_do_response = ToDoController.build_to_do_response(to_do_list[i], status_to_do_list[i], tag_to_do_list[i])
            response.append(to_do_response)
        return response
    
    @staticmethod
    def build_to_do_response(to_do, status, tag_list):
        to_do_dict = to_do.to_dict()
        to_do_dict['status'] = status.to_dict()
        to_do_dict['tags'] = [tag.to_dict() for tag in tag_list]
        response = ToDoResponse.parse_obj(to_do_dict)
        return response