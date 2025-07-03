from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Absence(Base):
    __tablename__ = "absences"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    date_debut = Column(DateTime, nullable=False)
    date_fin = Column(DateTime, nullable=False)
    remplacant = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
