# models/course.py
from pydantic import BaseModel, Field
from typing import Optional

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[float] = 0.0
    instructor_id: str

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    instructor_id: Optional[str] = None

class CourseInDB(CourseBase):
    id: str = Field(..., alias="id")
