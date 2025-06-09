from models.lessonschedule import Lessonschedule
from sqladmin import ModelView

class LessonScheduleAdmin(ModelView,model = Lessonschedule):
    column_list = [Lessonschedule.id, Lessonschedule.name, Lessonschedule.room, Lessonschedule.teacher, Lessonschedule.status]
    name_plural = "Lessonschedule"