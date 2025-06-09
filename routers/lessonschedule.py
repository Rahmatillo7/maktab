from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import database
from models.users import Users
from routers.login import get_current_user
from schema.lessonschedule import CreateLessonschedule, UpdateLessonschedule
from models.lessonschedule import Lessonschedule
from functions.lessonschedule import lesson_post,lesson_delete,lessson_put

routers_lesson = APIRouter(tags=["Lesson"])


@routers_lesson.get('/get_lesson')
def lesson_kurishi(db: Session = Depends(database)):
    return db.query(Lessonschedule).all()

@routers_lesson.post('/post_lesson')
def lesson_qushish(form: CreateLessonschedule, db: Session = Depends(database),
                   current_user: Users = Depends(get_current_user)):
    return lesson_post(form,db,current_user)

@routers_lesson.put('/put_lesson')
def lesson_yangilash(ident: int, form: UpdateLessonschedule, db: Session = Depends(database),
                     current_user: Users = Depends(get_current_user)):
    return lessson_put(ident,form,db,current_user)

@routers_lesson.delete('/delete_lesson')
def lesson_uchirish(ident: int, db: Session = Depends(database),
                    current_user: Users = Depends(get_current_user)):
    return lesson_delete(ident,db,current_user)

