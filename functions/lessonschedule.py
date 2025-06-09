from fastapi import HTTPException
from models.lessonschedule import Lessonschedule

def lesson_post(form,db, current_user):

    if current_user.role == 'admin':
        new = Lessonschedule(
            name = form.name,
            room = form.room,
            teacher = form.teacher,
            time = form.time,
            duration = form.duration,
            status = form.status,
            start_time = form.start_time,
            access_time = form.access_time,
            notes = form.notes
        )
        db.add(new)
        db.commit()
        return {"Message": "Lesseons qoshildi !!! "}
    else:
        raise HTTPException(400, "Siz admin emassiz!")

def lessson_put(ident,form,db,current_user):
    put = db.query(Lessonschedule).filter(Lessonschedule.id == ident).first()
    if not put:
        raise HTTPException(404, "Bunday id li mavjud emas !!! ")
    if current_user.role == 'admin':
        db.query(Lessonschedule).filter(Lessonschedule.id == ident).update({
            Lessonschedule.name : form.name,
            Lessonschedule.room : form.room,
            Lessonschedule.teacher : form.teacher,
            Lessonschedule.time : form.time,
            Lessonschedule.duration : form.duration,
            Lessonschedule.status : form.status,
            Lessonschedule.start_time : form.start_time,
            Lessonschedule.access_time : form.access_time,
            Lessonschedule.notes : form.notes
        })
        db.commit()
        return {"Message": "Lesson yangilandi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasiz 😔")

def lesson_delete(ident,db,current_user):
    delete = db.query(Lessonschedule).filter(Lessonschedule.id == ident).filter()
    if not delete:
        raise HTTPException(404, "Bunday id li mavjud emas")

    if current_user.role == 'admin':
        db.query(Lessonschedule).filter(Lessonschedule.id == ident).delete()
        db.commit()
        return {"Message": "Lesson uchirildi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasiz 😔")