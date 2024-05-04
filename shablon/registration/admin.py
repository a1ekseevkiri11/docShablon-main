from django.contrib import admin

from user.models import (
    Student,
    SupervisorPractice,
    SupervisorOPOP
)

admin.site.register(Student)
admin.site.register(SupervisorPractice)
admin.site.register(SupervisorOPOP)