from fastapi import FastAPI
from routes.app_ruotes import home
import uvicorn

app = FastAPI()

app.include_router(home)

if __name__ == "__main__":
    uvicorn.run(app=app)