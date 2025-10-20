# routers/enrollment.py
from fastapi import APIRouter, HTTPException
from models.enrollment import EnrollmentCreate
import crud.enrollment as crud

router = APIRouter()

@router.get("/", summary="List all enrollments")
async def list_enrollments():
    return await crud.list_enrollments()

@router.post("/", summary="Enroll a student")
async def enroll(payload: EnrollmentCreate):
    created = await crud.create_enrollment(payload)
    if not created:
        raise HTTPException(status_code=400, detail="Invalid student_id or course_id")
    return created

@router.delete("/{id}", summary="Remove enrollment")
async def remove_enrollment(id: str):
    ok = await crud.delete_enrollment(id)
    if not ok:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return {"deleted": True}

@router.get("/students/{id}/courses", summary="Get student's courses")
async def student_courses(id: str):
    return await crud.get_courses_by_student(id)

@router.get("/courses/{id}/students", summary="Get course's students")
async def course_students(id: str):
    return await crud.get_students_by_course(id)
