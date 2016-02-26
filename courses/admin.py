from django.contrib import admin

from .models import Course, Module, Section, Question, Progress

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Progress)
# Register your models here.
