from models.mavzular import Mavzular
from sqladmin import ModelView

class MavzularAdmin(ModelView, model = Mavzular):
    column_list = [Mavzular.id, Mavzular.name, Mavzular.fan_id, Mavzular.text]
    name_plural = "Mavzular"