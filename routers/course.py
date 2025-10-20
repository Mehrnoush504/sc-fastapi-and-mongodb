# routers/course.py
from fastapi import APIRouter, HTTPException
from typing import List
from models.course import CourseCreate, CourseUpdate
import crud.course as crud
import crud.instructor as instructor_crud

router = APIRouter()

@router.get("/", summary="List all courses")
async def list_courses():
    return await crud.list_courses()

@router.post("/", summary="Create a course")
async def create_course(payload: CourseCreate):
    # verify instructor exists
    inst = await instructor_crud.get_instructor(payload.instructor_id)
    if not inst:
        raise HTTPException(status_code=400, detail="Instructor not found")
    return await crud.create_course(payload)

@router.get("/{id}", summary="Get course by ID")
async def get_course(id: str):
    c = await crud.get_course(id)
    if not c:
        raise HTTPException(status_code=404, detail="Course not found")
    return c

@router.put("/{id}", summary="Update course")
async def update_course(id: str, payload: CourseUpdate):
    c = await crud.update_course(id, payload)
    if not c:
        raise HTTPException(status_code=404, detail="Course not found")
    return c

@router.delete("/{id}", summary="Delete course")
async def delete_course(id: str):
    ok = await crud.delete_course(id)
    if not ok:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"deleted": True}

@router.get("/instructor/{id}/courses", summary="Get all courses by instructor")
async def get_by_instructor(id: str):
    return await crud.list_courses_by_instructor(id)
