from sqlalchemy.orm import Session
from app.models.employees import Employee
from app.schemas.employee import EmployeeCreate
from app.utils.logger import logger

def create_employee(db: Session, emp: EmployeeCreate):
    employee = Employee(**emp.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    logger.info(f"Created employee ID {employee.id}")
    return employee

def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def update_employee(db: Session, employee_id: int, emp: EmployeeCreate):
    employee = get_employee(db, employee_id)
    if not employee:
        return None
    for field, value in emp.dict().items():
        setattr(employee, field, value)
    db.commit()
    db.refresh(employee)
    return employee

def delete_employee(db: Session, employee_id: int):
    employee = get_employee(db, employee_id)
    if not employee:
        return False
    db.delete(employee)
    db.commit()
    return True

def get_all_employees(db: Session):
    return db.query(Employee).all()
