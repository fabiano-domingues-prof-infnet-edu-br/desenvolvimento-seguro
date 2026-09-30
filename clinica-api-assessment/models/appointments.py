from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Appointment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int = Field(foreign_key="patient.id")
    professional_id: int = Field(foreign_key="user.id")
    date_time: datetime
    status: str = Field(default="agendada")  # agendada, cancelada, concluida
    notes: Optional[str] = None

class AppointmentCreate(SQLModel):
    patient_id: int
    professional_id: int
    date_time: datetime
    notes: Optional[str] = None