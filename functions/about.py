from models.about import About
from fastapi import HTTPException

def post_about(form,db,current_user):
    if current_user.role != 'admin':
        new = About(
            text = form.text,
            fan_id  = form.fan_id
        )
        db.add(new)
        db.commit()
        return {"Message": "About qushildi !!! "}
    else:
        raise HTTPException(400,"Siz admin emasz !!! ")


def put_yangilash(ident, form, db, current_user):

    a = db.query(About).filter(About.id == ident).first()
    if not a:
        raise HTTPException(404, "Siz qidirgan id li mavjud emas !!! ")

    if current_user.role != 'admin':
        db.query(About).filter(About.id == ident).update({
            About.text : form.text,
            About.fan_id : form.fan_id
        })
        db.commit()
        return {"Message": "About yangilandi !!! "}
    else:
        raise HTTPException(400,"Siz admin emasz")


def delete_uchirsh(ident,db,current_user):

    delete = db.query(About).filter(About.id == ident).first()
    if not delete:
        raise HTTPException(404,"Siz qidirgan id li mavjud emas !!! ")

    if current_user.role != 'admin':
        db.query(About).filter(About.id == ident).delete()
        db.commit()
        return {"Message": "Abount uchirildi !!! "}
    else:
        raise HTTPException(400,"Siz admin emasiz !!! ")