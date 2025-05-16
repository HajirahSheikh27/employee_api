from fastapi import FastAPI
from app.routes import employee, auth

app = FastAPI()

app.include_router(employee.router)
app.include_router(auth.router)
