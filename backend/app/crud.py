from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def create_absence(db: Session, absence: schemas.AbsenceCreate):
    new_abs = models.Absence(
        nom=absence.nom,
        date_debut=absence.date_debut,
        date_fin=absence.date_fin,
        remplacant=absence.remplacant,
        created_at=datetime.utcnow()
    )
    db.add(new_abs)
    db.commit()
    db.refresh(new_abs)
    return new_abs

def get_absences(db: Session):
    return db.query(models.Absence).all()
