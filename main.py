import fastapi
import uvicorn

from api import calc
from views import home

api = fastapi.FastAPI()

api.include_router(home.router)
api.include_router(calc.router)

if __name__ == '__main__':
    uvicorn.run(api, host="127.0.0.1", port=8000)
