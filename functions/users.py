from models.users import Users
from routers.login import HTTPException,get_password_hash

def user_post(form,db):
    new = Users(
        name=form.name,
        username=form.username,
        password=get_password_hash(form.password),
        address=form.address,
        number=form.number,
        email=form.email,
        role='admin'
    )
    db.add(new)
    db.commit()
    return {"Message": "Users qushildi !!! "}


def oqtuvchi_post(form, db, current_user):
    if current_user.role == 'admin':
        new = Users(
            name=form.name,
            username=form.username,
            password=get_password_hash(form.password),
            address=form.address,
            number=form.number,
            email=form.email,
            role='oqituvchi'
        )
        db.add(new)
        db.commit()
        return {"Message": "O'qituvchi muvaffaqiyatli qo'shildi!"}
    else:
        raise HTTPException(404, "Siz admin emassiz!")



def user_put(ident,form,db,current_user):
    a = db.query(Users).filter(Users.id == ident).first()
    if not a:
        raise HTTPException(404,"Siz qidirgan id li mavjud emas !!! ")

    if current_user.role =='admin':

        users = db.query(Users).filter(Users.id == ident).first()
        if not users:
            raise HTTPException(404,"Siz kiritgan user mavjud emas !! ")

        db.query(Users).filter(Users.id == ident).update({
            Users.name : form.name,
            Users.username : form.username,
            Users.password : form.password,
            Users.address : form.address,
            Users.number : form.number,
            Users.email : form.email
         })
        db.commit()
        return {"Message": "Users qushildi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")


def users_put(ident,form,db,current_user):

    q = db.query(Users).filter(Users.id == ident).first()
    if not q:
        raise HTTPException(404,"Siz qidirgan id li mavjud emas !!! ")

    if current_user.role =='admin':

        users = db.query(Users).filter(Users.id == ident).first()
        if not users:
            raise HTTPException(404,"Siz kiritgan user mavjud emas !! ")

        db.query(Users).filter(Users.id == ident).update({
            Users.name : form.name,
            Users.username : form.username,
            Users.password : form.password,
            Users.address : form.address,
            Users.number : form.number,
            Users.email : form.email
         })
        db.commit()
        return {"Message": "Users qushildi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")



def user_delete(ident,db,current_user):
    delete = db.query(Users).filter(Users.id == ident).first()
    if not delete:
        raise HTTPException(404,"Siz qidirgan id li mavjud emas !!! ")

    if current_user.role == 'admin':

        user = db.query(Users).filter(Users.id == ident).first()
        if not user:
            raise HTTPException(404,"Siz kiritgan user mavjud emas !! ")

        db.query(Users).filter(Users.id == ident).delete()
        db.commit()
        return {"Message": "Users uchirildi"}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")


def users_delete(ident,db,current_user):
    deletes = db.query(Users).filter(Users.id == ident).first()
    if not deletes:
        raise HTTPException(404,"Siz qidirgan id li mavjud emas !!! ")

    if current_user.role == 'admin':

        user = db.query(Users).filter(Users.id == ident).first()
        if not user:
            raise HTTPException(404,"Siz kiritgan user mavjud emas !! ")

        db.query(Users).filter(Users.id == ident).delete()
        db.commit()
        return {"Message": "Users uchirildi"}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")


