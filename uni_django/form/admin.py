from django.contrib import admin

from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8')


admin.site.register(Form, FormAdmin)
# Register your models here.
