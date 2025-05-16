from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas.employee import Employee, EmployeeCreate
from app.crud import employee as crud
from app.auth.dependencies import require_role

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model=Employee, dependencies=[Depends(require_role(["admin"]))])
def create(emp: EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, emp)

@router.get("/", response_model=list[Employee], dependencies=[Depends(require_role(["admin", "viewer"]))])
def read_all(db: Session = Depends(get_db)):
    return crud.get_all_employees(db)

@router.get("/{id}", response_model=Employee, dependencies=[Depends(require_role(["admin", "viewer"]))])
def read(id: int, db: Session = Depends(get_db)):
    emp = crud.get_employee(db, id)
    if not emp:
        raise HTTPException(404, detail="Not found")
    return emp

@router.put("/{id}", response_model=Employee, dependencies=[Depends(require_role(["admin"]))])
def update(id: int, emp: EmployeeCreate, db: Session = Depends(get_db)):
    updated = crud.update_employee(db, id, emp)
    if not updated:
        raise HTTPException(404, detail="Not found")
    return updated

@router.delete("/{id}", dependencies=[Depends(require_role(["admin"]))])
def delete(id: int, db: Session = Depends(get_db)):
    if not crud.delete_employee(db, id):
        raise HTTPException(404, detail="Not found")
    return {"detail": "Deleted"}
