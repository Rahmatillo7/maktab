from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from functions.about import post_about,put_yangilash,delete_uchirsh
from models.users import Users
from functions.about import HTTPException
from routers.login import get_current_user
from schema.about import CreateAbout,UpdateAbout
from models.about import About
from db import database

routers_about = APIRouter(tags=["About"])

@routers_about.get('/get_about')
def about_kurish(db: Session = Depends(database)):
    return db.query(About).all()

@routers_about.post('/post_about')
def about_qushish(form: CreateAbout,db: Session = Depends(database),
                  current_user: Users = Depends(get_current_user)):
    return post_about(form,db,current_user)

@routers_about.put('/put_about')
def about_yangilash(ident: int, form: UpdateAbout,db: Session = Depends(database),
                    current_user: Users = Depends(get_current_user)):
    return put_yangilash(ident,form,db,current_user)

@routers_about.delete('/delete_uchirsh')
def about_delete(ident: int, db: Session = Depends(database),
                 current_user: Users = Depends(get_current_user)):
    return delete_uchirsh(ident,db,current_user)