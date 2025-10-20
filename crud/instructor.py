# crud/instructor.py
from bson import ObjectId
from database import instructors_collection
from typing import List, Optional
from models.instructor import InstructorCreate, InstructorUpdate
from utils import obj_to_id

async def create_instructor(instructor: InstructorCreate) -> dict:
    doc = instructor.dict()
    result = await instructors_collection.insert_one(doc)
    doc["_id"] = result.inserted_id
    return obj_to_id(doc)

async def list_instructors() -> List[dict]:
    cursor = instructors_collection.find()
    items = []
    async for doc in cursor:
        items.append(obj_to_id(doc))
    return items

async def get_instructor(instructor_id: str) -> Optional[dict]:
    doc = await instructors_collection.find_one({"_id": ObjectId(instructor_id)})
    return obj_to_id(doc) if doc else None

async def update_instructor(instructor_id: str, data: InstructorUpdate) -> Optional[dict]:
    update_data = {k:v for k,v in data.dict().items() if v is not None}
    if not update_data:
        return await get_instructor(instructor_id)
    await instructors_collection.update_one({"_id": ObjectId(instructor_id)}, {"$set": update_data})
    return await get_instructor(instructor_id)

async def delete_instructor(instructor_id: str) -> bool:
    res = await instructors_collection.delete_one({"_id": ObjectId(instructor_id)})
    return res.deleted_count == 1
