from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models.users import Users
from routers.login import get_current_user
from schema.mavzular import UpdateMavzular,CreateMavzular
from models.mavzular import Mavzular
from functions.mavzular import put_mavzu,post_mavzu,delete_mavzu
from db import database

routers_mavzu = APIRouter(tags=["Mavzular"])


@routers_mavzu.get('/get')
def mavzu_kurish(db: Session = Depends(database)):
    return db.query(Mavzular).all()


@routers_mavzu.post('/post')
def mavzu_qushish(form: CreateMavzular,db: Session = Depends(database),
                  current_user: Users = Depends(get_current_user)):
    return post_mavzu(form,db,current_user)


@routers_mavzu.put('/put')
def mavzu_yangilash(ident: int, form: UpdateMavzular,db: Session = Depends(database),
                    current_user: Users = Depends(get_current_user)):
    return put_mavzu(ident,form,db,current_user)



@routers_mavzu.delete('/delete_mavzu')
def mavzu_uchirish(ident: int,db: Session = Depends(database),
                  current_user: Users = Depends(get_current_user)):
    return delete_mavzu(ident,db,current_user)