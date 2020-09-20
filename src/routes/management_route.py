from .session_route import SessionRoute
from .status_route import StatusRoute
class ManagementRoute:
    routers = [SessionRoute.router,StatusRoute.router]