from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routes.classroom_route import classroom_router
from src.routes.course_route import course
from src.routes.degree_route import degree
from src.routes.login_route import login
from src.routes.schedule_route import schedule
from src.routes.student_route import student
from src.routes.subject_route import subject
from src.routes.teacher_route import teacher
from src.routes.user_route import user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login, prefix="/login")
app.include_router(degree, prefix="/degree")
app.include_router(subject, prefix="/subject")
app.include_router(teacher, prefix="/teacher")
app.include_router(student, prefix="/student")
app.include_router(course, prefix="/course")
app.include_router(user, prefix="/user")
app.include_router(classroom_router, prefix="/classroom")
app.include_router(schedule, prefix="/schedule")