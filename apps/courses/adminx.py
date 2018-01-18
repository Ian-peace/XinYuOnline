# _*_ encoding:utf-8 _*_
__auther__ = 'Demon'
__date__ = '2018/1/18 17:05'
import xadmin

from .models import Course, CourseResource, Lesson, Video


class CourseAdmin(object):
    list_display = ['name', 'describe', 'detail', 'degree', 'learning_time', 'students_nums', 'collection_nums',
                    'image', 'click_nums', 'add_time']
    search_fields = ['name', 'describe', 'degree', 'students_nums', 'collection_nums', 'click_nums']
    list_filter = ['name', 'degree', 'learning_time', 'students_nums', 'collection_nums', 'click_nums', 'add_time']


class LessonAdmin(object):
    list_display = ['course', 'chapter', 'add_time']
    search_fields = ['course', 'chapter']
    list_filter = ['course__name', 'chapter', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__chapter', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
