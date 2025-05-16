# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from app.models.users import User
# from app.schemas.users import UserLogin, UserOut, UserCreate
# from app.db import get_db
# from app.auth.jwt_handler import create_jwt_token

# router = APIRouter(tags=["Auth"])

# @router.post("/register", response_model=UserOut)
# def register(user: UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(User).filter(User.username == user.username).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Username already exists")
    
#     if user.role not in ["admin", "user"]:
#         raise HTTPException(status_code=400, detail="Role must be 'admin' or 'user'")
    
#     new_user = User(username=user.username, password=user.password, role=user.role)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @router.post("/login")
# def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.username == user.username).first()
#     if not db_user or db_user.password != user.password:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     token = create_jwt_token(db_user.id, db_user.username, db_user.role)
#     return {"access_token": token, "token_type": "bearer"}


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import UserLogin, UserOut, UserCreate
from app.db import get_db
from app.auth.jwt_handler import create_jwt_token

router = APIRouter(tags=["Auth"])

# Hardcoded admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "supersecretpassword"  # change this to your preferred password
ADMIN_ROLE = "admin"
ADMIN_ID = 1  # fixed admin user id for token payload

# Remove or comment this out to disable registration
# @router.post("/register", response_model=UserOut)
# def register(user: UserCreate, db: Session = Depends(get_db)):
#     raise HTTPException(status_code=403, detail="Registration disabled")

@router.post("/login")
def login(user: UserLogin):
    if user.username == ADMIN_USERNAME and user.password == ADMIN_PASSWORD:
        token = create_jwt_token(ADMIN_ID, ADMIN_USERNAME, ADMIN_ROLE)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
