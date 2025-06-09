from models.lessonschedule import Lessonschedule
from sqladmin import ModelView

class LessonScheduleAdmin(ModelView,model = Lessonschedule):
    column_list = [Lessonschedule.id, Lessonschedule.name, Lessonschedule.room, Lessonschedule.teacher, Lessonschedule.time, Lessonschedule.start_time, Lessonschedule.duration, Lessonschedule.status, Lessonschedule.access_time, Lessonschedule.notes]
    name_plural = "Lessonschedule"