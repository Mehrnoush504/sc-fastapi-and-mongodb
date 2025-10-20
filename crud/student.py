# crud/student.py
from bson import ObjectId
from database import students_collection
from typing import List, Optional
from models.student import StudentCreate, StudentUpdate
from utils import obj_to_id

async def create_student(student: StudentCreate) -> dict:
    doc = student.dict()
    res = await students_collection.insert_one(doc)
    doc["_id"] = res.inserted_id
    return obj_to_id(doc)

async def list_students() -> List[dict]:
    cursor = students_collection.find()
    items = []
    async for doc in cursor:
        items.append(obj_to_id(doc))
    return items

async def get_student(student_id: str) -> Optional[dict]:
    doc = await students_collection.find_one({"_id": ObjectId(student_id)})
    return obj_to_id(doc) if doc else None

async def update_student(student_id: str, data: StudentUpdate) -> Optional[dict]:
    update_data = {k:v for k,v in data.dict().items() if v is not None}
    if update_data:
        await students_collection.update_one({"_id": ObjectId(student_id)}, {"$set": update_data})
    return await get_student(student_id)

async def delete_student(student_id: str) -> bool:
    res = await students_collection.delete_one({"_id": ObjectId(student_id)})
    return res.deleted_count == 1
