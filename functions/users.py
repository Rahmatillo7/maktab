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
        role='users'
    )
    db.add(new)
    db.commit()
    return {"Message": "Users qushildi !!! "}


def oqtuvchi_post(form,db,current_user):

    if current_user.role =='oqituvchi':
        new = Users(
            name=form.name,
            username=form.username,
            password=get_password_hash(form.password),
            address=form.address,
            number = form.number,
            email=form.email,
            role='oqtuvchi'
        )
        db.add(new)
        db.commit()
        return {"Message": "Users qushildi !!! "}
    else:
        raise HTTPException(404,"Siz admin emsiz !!! ")


def user_put(ident,form,db,current_user):
    a = db.query(Users).filter(Users.id == ident).first()
    if not a:
        raise HTTPException(404,"Siz qidirgan id li mavjud emas !!! ")

    if current_user.role =='admin':

        users = db.query(Users).filter(Users.id == form).first()
        if not users:
            raise HTTPException(404,"Siz kiritgan user mavjud emas !! ")

        db.query(Users).filter(Users.id == ident).update({
            Users.name : form.name,
            Users.username : form.username,
            Users.password : form.password,
            Users.token : form.token,
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