# database.py
import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DB", "course_db")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# helper: collections
instructors_collection = db.get_collection("instructors")
courses_collection = db.get_collection("courses")
students_collection = db.get_collection("students")
enrollments_collection = db.get_collection("enrollments")
