from .session_route import SessionRoute
from .status_route import StatusRoute
from .tag_route import TagRoute
from .to_do_route import ToDoRoute
class ManagementRoute:
    routers = [SessionRoute.router,StatusRoute.router,TagRoute.router,ToDoRoute.router]