from django.contrib import admin
from course.models import Course, Subject
from home.models import Setting

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Setting)
