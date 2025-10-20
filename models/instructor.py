# models/instructor.py
from pydantic import BaseModel, Field
from typing import Optional

class InstructorBase(BaseModel):
    name: str
    bio: Optional[str] = None
    email: Optional[str] = None

class InstructorCreate(InstructorBase):
    pass

class InstructorUpdate(BaseModel):
    name: Optional[str] = None
    bio: Optional[str] = None
    email: Optional[str] = None

class InstructorInDB(InstructorBase):
    id: str = Field(..., alias="id")
