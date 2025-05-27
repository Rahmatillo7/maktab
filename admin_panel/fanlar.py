from models.fanlar import Fanlar
from sqladmin import ModelView

class FanlarAdmin(ModelView, model = Fanlar):
    column_list = [Fanlar.id, Fanlar.nomi]

    name_plural = "Fanlar"