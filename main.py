# main.py
from fastapi import FastAPI
from routers import instructor, course, student, enrollment

app = FastAPI(title="Course Selling API")

app.include_router(instructor.router, prefix="/instructors", tags=["Instructors"])
app.include_router(course.router, prefix="/courses", tags=["Courses"])
app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(enrollment.router, prefix="/enrollments", tags=["Enrollments"])
