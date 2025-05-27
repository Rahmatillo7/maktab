from models.users import Users
from sqladmin import ModelView

class UsersAdmin(ModelView, model = Users):

    column_list = [Users.id , Users.name, Users.username, Users.password, Users.number, Users.address,Users.email,Users.role]
    name_plural = 'Users'