# models/enrollment.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class EnrollmentBase(BaseModel):
    student_id: str
    course_id: str

class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentInDB(EnrollmentBase):
    id: str = Field(..., alias="id")
    enrolled_at: datetime
