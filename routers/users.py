from fastapi import APIRouter,Depends,HTTPException,Request
from sqlalchemy.orm import Session
from db import database
from schema.users import CreateUsers,UpdateUsers
from models.users import Users
from functions.users import user_post,admin_post,users_put,user_delete
from routers.login import get_current_active_user
from fastapi import UploadFile
from utlis.save_file import save_file

routers_users = APIRouter(tags=["Users"])


@routers_users.get('/users_kurish')
def get_kurish(db:Session = Depends(database)):
    return db.query(Users).all()


@routers_users.post('/post_users')
def post_user(form: CreateUsers,db: Session = Depends(database)):
    return user_post(form,db)


@routers_users.post('/admin_post')
def adminn_post(form: CreateUsers,db: Session = Depends(database),
                 current_user: Users = Depends(get_current_active_user)):
    return admin_post(form,db,current_user)


@routers_users.put('/admin_yagilash')
def users_yangilash(ident: int ,form: UpdateUsers,db: Session = Depends(database),
                  current_user: Users = Depends(get_current_active_user)):
    return users_put(ident,form,db,current_user)



@routers_users.post("/admin/login")
async def login(request: Request, auth_backend=None):
    if await auth_backend.login(request):
        return {"message": "Admin login successful"}
    return {"error": "Invalid admin credentials"}


@routers_users.delete('/delete')
def user_deletes(ident: int ,db: Session = Depends(database),
                current_user: Users = Depends(get_current_active_user)):
    return user_delete(ident, db,current_user)



@routers_users.put('/images')
def rasm_qushish(ident: int,file: UploadFile,db: Session = Depends(database),
        current_user: Users = Depends(get_current_active_user)):
    user = db.query(Users).filter(Users.id == ident).first()
    if not user:
        raise HTTPException(404, "Siz qidirgan foydalanuvchi topilmadi")

    user.images = save_file(file)
    db.commit()
    return {"message": "Rasm qo‘shildi!"}


