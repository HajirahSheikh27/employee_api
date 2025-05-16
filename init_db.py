from app.db import engine
from app.models.users import User
from app.models.employees import Employee
from app.db import Base

# Create all tables
Base.metadata.create_all(bind=engine)
