from models.fanlar import Fanlar
from fastapi import HTTPException


def post_fan(form, db, current_user):
    if current_user.role != 'admin':
        new_subject = Fanlar(
            nomi = form.nomi,
        )
        db.add(new_subject)
        db.commit()
        return {"message": "Yangi mavzu muvaffaqiyatli qo'shildi!"}
    else:
        raise HTTPException(400, "Siz admin emassiz!")

def put_fan(ident ,form, db, current_user):

    a = db.query(Fanlar).filter(Fanlar.id == ident).first()
    if not a:
        raise HTTPException(404, "Siz qidirgan id li mavjud emas !!! ")

    if current_user.role != 'admin':
        db.query(Fanlar).filter(Fanlar.id == ident).update({
            Fanlar.nomi: form.nomi,
        })
        db.commit()
        return {'message' : "Mavzu tahrirlangan!"}
    else:
        raise HTTPException(400, "Siz admin emassiz!")

def delete_fan(ident, db, current_user):
    delete = db.query(Fanlar).filter(Fanlar.id == ident).first()
    if not delete:
        raise HTTPException(404,"Siz qidirgan id li mavjud emas !!! ")
    if current_user.role != 'admin':
        db.query(Fanlar).filter(Fanlar.id == ident).delete()
        db.commit()
        return {'message': "Mavzu allaqachon olib tashlangan!"}
    else:
        raise HTTPException(400, "Siz admin emassiz!")