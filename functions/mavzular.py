from http.client import HTTPException
from models.mavzular import Mavzular
from fastapi import HTTPException

def post_mavzu(form, db, current_user):
    if current_user.role != 'admin':
        new = Mavzular(
            name=form.name,
            fan_id = form.fan_id,
            text = form.text
        )
        db.add(new)
        db.commit()
        return {"message": "Mavzular qo‘shildi!"}
    else:
        raise HTTPException(403, "Siz admin emassiz!")


def put_mavzu(ident,form,db,current_user):
    if current_user.role != 'admin':
        db.query(Mavzular).filter(Mavzular.id == ident).update({
            Mavzular.name : form.name,
            Mavzular.fan_id : form.fan_id,
            Mavzular.text : form.text
        })
        db.commit()
        return {"Message": "Mavzular yangilandi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")

def delete_mavzu(ident,db,current_user):
    if current_user.role !='admin':
        db.query(Mavzular).filter(Mavzular.id == ident).delete()
        db.commit()
        return {"Message": "Mavzular uchirldi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")
