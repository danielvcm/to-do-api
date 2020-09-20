from .session_route import SessionRoute
from .status_route import StatusRoute
from .tag_route import TagRoute
class ManagementRoute:
    routers = [SessionRoute.router,StatusRoute.router,TagRoute.router]