from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
from database.connection import get_session
from models.appointments import Appointment, AppointmentCreate
from auth.rbac import RoleChecker
from models.users import User

appointment_router = APIRouter(tags=["Appointments"])

allow_create = RoleChecker(["admin", "recepcionista"])
allow_read = RoleChecker(["admin", "recepcionista", "profissional"])

@appointment_router.post("/new", response_model=Appointment)
async def create_appointment(
    data: AppointmentCreate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(allow_create)
):
    # Desafio para os alunos: Adicionar validação se o horário já está ocupado!
    new_appointment = Appointment(**data.dict())
    session.add(new_appointment)
    session.commit()
    session.refresh(new_appointment)
    return new_appointment

@appointment_router.get("/", response_model=List[Appointment])
async def list_appointments(
    session: Session = Depends(get_session),
    current_user: User = Depends(allow_read)
):
    appointments = session.exec(select(Appointment)).all()
    return appointments