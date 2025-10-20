# crud/course.py
from bson import ObjectId
from database import courses_collection
from typing import List, Optional
from models.course import CourseCreate, CourseUpdate
from utils import obj_to_id
from motor.motor_asyncio import AsyncIOMotorCollection

async def create_course(course: CourseCreate) -> dict:
    doc = course.dict()
    res = await courses_collection.insert_one(doc)
    doc["_id"] = res.inserted_id
    return obj_to_id(doc)

async def list_courses() -> List[dict]:
    cursor = courses_collection.find()
    items = []
    async for doc in cursor:
        items.append(obj_to_id(doc))
    return items

async def get_course(course_id: str) -> Optional[dict]:
    doc = await courses_collection.find_one({"_id": ObjectId(course_id)})
    return obj_to_id(doc) if doc else None

async def update_course(course_id: str, data: CourseUpdate) -> Optional[dict]:
    update_data = {k:v for k,v in data.dict().items() if v is not None}
    if update_data:
        await courses_collection.update_one({"_id": ObjectId(course_id)}, {"$set": update_data})
    return await get_course(course_id)

async def delete_course(course_id: str) -> bool:
    res = await courses_collection.delete_one({"_id": ObjectId(course_id)})
    return res.deleted_count == 1

async def list_courses_by_instructor(instructor_id: str) -> List[dict]:
    cursor = courses_collection.find({"instructor_id": instructor_id})
    items = []
    async for doc in cursor:
        items.append(obj_to_id(doc))
    return items
