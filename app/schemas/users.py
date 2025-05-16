from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str
    role: str  # Must be "admin" or "user"
