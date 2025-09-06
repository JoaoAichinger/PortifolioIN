from fastapi import FastAPI

app = FastAPI()

#from routes.student_routes import student_router
#from routes.project_routes import project_router
from routes.user_routes import user_router

#app.include_router(student_router)
#app.include_router(project_router)
app.include_router(user_router)