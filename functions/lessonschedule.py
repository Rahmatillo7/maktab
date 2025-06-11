from fastapi import HTTPException
from models.lessonschedule import Lessonschedule

def lesson_post(form, db, current_user):

    if current_user.role == 'admin':
        new = Lessonschedule(
            name = form.name,
            room = form.room,
            teacher = form.teacher,
            status = form.status,
            day_name = form.day_name,
            lesson_date = form.lesson_date,
            start_time = form.start_time
        )
        db.add(new)
        db.commit()
        return {"Message": "Lesseons qoshildi !!! "}
    else:
        raise HTTPException(400, "Siz admin emassiz!")



def lessson_put(ident, form, db, current_user):

    pov = db.query(Lessonschedule).filter(Lessonschedule.id == ident).first()
    if not pov:
        raise HTTPException(404, "Bunday id li dars mavjud emas!")

    if current_user.role == 'admin':
        db.query(Lessonschedule).filter(Lessonschedule.id == ident).update({
            Lessonschedule.name: form.name,
            Lessonschedule.room: form.room,
            Lessonschedule.teacher: form.teacher,
            Lessonschedule.status: form.status,
            Lessonschedule.day_name: form.day_name,
            Lessonschedule.lesson_date: form.lesson_date,
            Lessonschedule.start_time: form.start_time
        })
        db.commit()
        return {"message": "Dars ma'lumotlari yangilandi ✅"}
    else:
        raise HTTPException(403, "Sizda bu amalni bajarish huquqi yo'q 😔")




def lesson_delete(ident,db,current_user):
    delet = db.query(Lessonschedule).filter(Lessonschedule.id == ident).filter()
    if not delet:
        raise HTTPException(404, "Bunday id li mavjud emas")

    if current_user.role == 'admin':
        db.query(Lessonschedule).filter(Lessonschedule.id == ident).delete()
        db.commit()
        return {"Message": "Lesson uchirildi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasiz 😔")






