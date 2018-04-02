from django.contrib import admin
from appuser.models import User,Course,Note


# Blog模型的管理器
class UserAdmin(admin.ModelAdmin):
    list_filter = ['username']
    search_fields = ['username']  # 添加快速查询栏

class CourseAdmin(admin.ModelAdmin):
    list_filter = ['cname','cid','uid']
    search_fields = ['cname','cid','uid']  # 添加快速查询栏

class NoteAdmin(admin.ModelAdmin):
    list_filter = ['nid', 'uid']
    search_fields = ['uid']  # 添加快速查询栏
# 在admin中注册绑定
admin.site.register(User, UserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Note,NoteAdmin)