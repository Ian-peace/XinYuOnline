# _*_ encoding:utf-8 _*_
__auther__ = 'Demon'
__date__ = '2018/1/18 17:41'
import xadmin

from .models import CourseComments, UserAsk, UserCollection, UserCourse, UserMessage


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course__name', 'comments', 'add_time']


class UserCollectionAdmin(object):
    list_display = ['user', 'collection_id', 'collection_type', 'add_time']
    search_fields = ['user', 'collection_id', 'collection_type']
    list_filter = ['user', 'collection_id', 'collection_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'is_read', 'add_time']
    search_fields = ['user', 'message', 'is_read']
    list_filter = ['user', 'message', 'is_read', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course__name', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserCollection, UserCollectionAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)