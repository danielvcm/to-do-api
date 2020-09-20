from dotenv import load_dotenv
load_dotenv()
import uvicorn
from fastapi import  FastAPI, Request
from fastapi.responses import JSONResponse
from src.routes.management_route import ManagementRoute
from src.utils.to_do_exception import ToDoException

to_do_api = FastAPI()

for router in ManagementRoute.routers:
    to_do_api.include_router(router)

@to_do_api.exception_handler(ToDoException)
async def to_do_exception_handler(request: Request, exc: ToDoException):
    return JSONResponse(content= exc.to_dict(),status_code=exc.status_code)

if __name__ == "__main__":
    uvicorn.run("app:to_do_api", host="127.0.0.1", port=5000, log_level="info",reload=True)