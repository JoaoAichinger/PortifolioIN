from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()


app = FastAPI(title= "Infinity API")


from routes.auth_routes import auth_router
from routes.project_routes import project_routes
from routes.students_routes import students_routes
from routes.tags_routes import tags_routes


app.include_router(auth_router)
app.include_router(project_routes)
app.include_router(students_routes)
app.include_router(tags_routes)

from schemas.auth_schemas import MessageOut

@app.get("/", response_model=MessageOut)
def root():
    return MessageOut(message="Welcome to Infinity API. Go to /docs to see the documentation.")