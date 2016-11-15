from django.contrib import admin
from project.models import Subject, Course, Lecture
# Register your models here.

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Lecture)