from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/absence", response_model=schemas.Absence)
def create_absence(absence: schemas.AbsenceCreate, db: Session = Depends(get_db)):
    return crud.create_absence(db=db, absence=absence)

@router.get("/absences", response_model=list[schemas.Absence])
def list_absences(db: Session = Depends(get_db)):
    return crud.get_absences(db)
