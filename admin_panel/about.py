from models.about import About
from sqladmin import ModelView

class AboutAdmin(ModelView,model = About):
    column_list = [About.id, About.text, About.fan_id]
    name_plural = "About"