# routers/student.py
from fastapi import APIRouter, HTTPException
from models.student import StudentCreate, StudentUpdate
import crud.student as crud

router = APIRouter()

@router.get("/", summary="List all students")
async def list_students():
    return await crud.list_students()

@router.post("/", summary="Create student")
async def create_student(payload: StudentCreate):
    return await crud.create_student(payload)

@router.get("/{id}", summary="Get student by ID")
async def get_student(id: str):
    s = await crud.get_student(id)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    return s

@router.put("/{id}", summary="Update student")
async def update_student(id: str, payload: StudentUpdate):
    s = await crud.update_student(id, payload)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    return s

@router.delete("/{id}", summary="Delete student")
async def delete_student(id: str):
    ok = await crud.delete_student(id)
    if not ok:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"deleted": True}
