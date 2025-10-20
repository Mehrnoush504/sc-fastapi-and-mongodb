# crud/enrollment.py
from bson import ObjectId
from database import enrollments_collection, students_collection, courses_collection
from typing import List, Optional
from models.enrollment import EnrollmentCreate
from utils import obj_to_id
from datetime import datetime

async def create_enrollment(enrollment: EnrollmentCreate) -> dict:
    # optional checks: student exists and course exists
    student = await students_collection.find_one({"_id": ObjectId(enrollment.student_id)})
    course = await courses_collection.find_one({"_id": ObjectId(enrollment.course_id)})
    if not student or not course:
        return None

    doc = {
        "student_id": enrollment.student_id,
        "course_id": enrollment.course_id,
        "enrolled_at": datetime.utcnow()
    }
    res = await enrollments_collection.insert_one(doc)
    doc["_id"] = res.inserted_id
    return obj_to_id(doc)

async def list_enrollments() -> List[dict]:
    cursor = enrollments_collection.find()
    items = []
    async for doc in cursor:
        items.append(obj_to_id(doc))
    return items

async def delete_enrollment(enrollment_id: str) -> bool:
    res = await enrollments_collection.delete_one({"_id": ObjectId(enrollment_id)})
    return res.deleted_count == 1

async def get_courses_by_student(student_id: str) -> List[dict]:
    cursor = enrollments_collection.find({"student_id": student_id})
    course_ids = []
    async for doc in cursor:
        course_ids.append(doc["course_id"])
    # fetch course docs
    courses = []
    for cid in course_ids:
        c = await courses_collection.find_one({"_id": ObjectId(cid)})
        if c:
            courses.append(obj_to_id(c))
    return courses

async def get_students_by_course(course_id: str) -> List[dict]:
    cursor = enrollments_collection.find({"course_id": course_id})
    student_ids = []
    async for doc in cursor:
        student_ids.append(doc["student_id"])
    students = []
    for sid in student_ids:
        s = await students_collection.find_one({"_id": ObjectId(sid)})
        if s:
            students.append(obj_to_id(s))
    return students
