# models/student.py
from pydantic import BaseModel, Field
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class StudentInDB(StudentBase):
    id: str = Field(..., alias="id")
