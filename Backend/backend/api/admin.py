from django.contrib import admin
from .models import Subject
# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
  list_display = ['id', 'subject', 'chapter', 'question', 'option01', 'option02', 'option03', 'option04', 'answer', 'board', 'univercity']
