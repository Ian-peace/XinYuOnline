# _*_ encoding:utf-8 _*_
__auther__ = 'Demon'
__date__ = '2018/1/18 17:54'
import xadmin

from .models import CityDict, Organization, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'describe', 'add_time']
    search_fields = ['name', 'describe']
    list_filter = ['name',  'add_time']


class OrganizationAdmin(object):
    list_display = ['name', 'describe', 'click_nums', 'collection_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'describe', 'click_nums', 'collection_nums', 'image', 'address', 'city']
    list_filter = ['name', 'click_nums', 'collection_nums', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['name', 'organization', 'work_years', 'work_company', 'work_position', 'Teach_Features',
                    'click_nums', 'collection_nums', 'add_time']
    search_fields = ['name', 'organization', 'work_years', 'work_company', 'work_position', 'Teach_Features',
                     'click_nums', 'collection_nums']
    list_filter = ['name', 'organization', 'work_years', 'work_company', 'work_position', 'click_nums',
                   'collection_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Organization, OrganizationAdmin)
xadmin.site.register(Teacher, TeacherAdmin)