# -*- coding:utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Grades, Students
# 注册
class StudentsInfo(admin.TabularInline):# 可选参数admin.StackedInline
    model = Students
    extra = 2

@admin.register(Grades)#装饰器注册
class GradesAdmin(admin.ModelAdmin):
    # 列表页属性
    inlines = [StudentsInfo]
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']  # 显示字段
    list_filter = ['gname']  # 过滤器
    search_fields = ['gname']  # 搜索
    list_per_page = 5  # 分页
    # 添加，修改页属性
    # fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']
    fieldsets = [
        ("base", {"fields": ["gname", "gdate", "isDelete"]}),
        ("num", {"fields": ['ggirlnum', 'gboynum']}),
    ]
    actions_on_top = False
    actions_on_bottom = True

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    # 设置页面列的名称
    gender.short_description = "性别"
    def name(self):
        if self.sname:
            return self.sname
    name.short_description = '名字'
    list_display = ['pk', name, 'sage', gender,'scontend', 'sgrade', 'isDelete']
    list_per_page = 10
    list_filter = ['sgrade','sgender']  # 过滤器
    search_fields = ['sname']  # 搜索
    actions_on_top = False
    actions_on_bottom = True

# 代码注册
# admin.site.register(Grades,GradesAdmin)
# admin.site.register(Students,StudentsAdmin)