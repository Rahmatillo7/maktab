from models.news import News
from sqladmin import ModelView

class NewsAdmin(ModelView,model = News):
    column_list = [News.id, News.text]
    name_plural = "News"