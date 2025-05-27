from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from routers.login import login_router, SECRET_KEY
from routers.users import routers_users
from admin_panel.fanlar import FanlarAdmin
from routers.news import routers_news
from admin_panel.about import AboutAdmin
from admin_panel.mavzular import MavzularAdmin
from admin_panel.users import UsersAdmin
from admin_panel.news import NewsAdmin
from db import engine
from admin_panel.login import AdminAuth
from sqladmin import Admin
from routers.fanlar import routers_fan
from routers.about import routers_about
from routers.mavzular import routers_mavzu
from db import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(SessionMiddleware, secret_key = SECRET_KEY)

app.include_router(routers_about)
app.include_router(routers_mavzu)
app.include_router(routers_fan)
app.include_router(login_router)
app.include_router(routers_users)
app.include_router(routers_news)

authentication_backend = AdminAuth(secret_key=SECRET_KEY)
admin = Admin(app,engine,authentication_backend=authentication_backend)

admin.add_model_view(FanlarAdmin)
admin.add_model_view(MavzularAdmin)
admin.add_model_view(UsersAdmin)
admin.add_model_view(AboutAdmin)
admin.add_model_view(NewsAdmin)