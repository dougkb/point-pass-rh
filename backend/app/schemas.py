from pydantic import BaseModel, Field
from datetime import datetime

class AbsenceBase(BaseModel):
    nom: str = Field(..., min_length=2, max_length=100, example="Bougary Kanté")
    date_debut: datetime = Field(..., example="2025-07-01T09:00:00")
    date_fin: datetime = Field(..., example="2025-07-05T17:00:00")
    remplacant: str = Field(..., min_length=2, max_length=100, example="Fatou Diouf")

class AbsenceCreate(AbsenceBase):
    pass

class Absence(AbsenceBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True  # remplace orm_mode pour Pydantic V2
    }
