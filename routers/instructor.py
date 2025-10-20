# routers/instructor.py
from fastapi import APIRouter, HTTPException
from typing import List
from models.instructor import InstructorCreate, InstructorUpdate
import crud.instructor as crud

router = APIRouter()

@router.get("/", summary="List all instructors")
async def list_instructors():
    return await crud.list_instructors()

@router.post("/", summary="Create instructor")
async def create_instructor(payload: InstructorCreate):
    return await crud.create_instructor(payload)

@router.get("/{id}", summary="Get instructor by ID")
async def get_instructor(id: str):
    inst = await crud.get_instructor(id)
    if not inst:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return inst

@router.put("/{id}", summary="Update instructor")
async def update_instructor(id: str, payload: InstructorUpdate):
    inst = await crud.update_instructor(id, payload)
    if not inst:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return inst

@router.delete("/{id}", summary="Delete instructor")
async def delete_instructor(id: str):
    ok = await crud.delete_instructor(id)
    if not ok:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return {"deleted": True}
