from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database
from functions.fanlar import post_fan,delete_fan,put_fan
from models.users import Users
from schema.fanlar import CreateFanlar, UpdateFanlar
from routers.login import get_current_user
from models.fanlar import Fanlar

routers_fan = APIRouter(tags=["Fanlar"])


@routers_fan.get('/get_fanlar')
def get_subject(db: Session = Depends(database)):
    return db.query(Fanlar).all()


@routers_fan.post('/post_fanlar')
def create_subject(form: CreateFanlar, db: Session = Depends(database),
                current_user: Users = Depends(get_current_user)):
    return post_fan(form, db, current_user)


@routers_fan.put('/sanlar_yangilash')
def update_subject(ident: int, form: UpdateFanlar, db: Session = Depends(database),
              current_user: Users = Depends(get_current_user)):
    return put_fan(ident,form, db, current_user)


@routers_fan.delete('/delete_fanlar')
def remove_subject(ident: int, db: Session = Depends(database),
                current_user: Users = Depends(get_current_user)):
    return delete_fan(ident, db, current_user)


