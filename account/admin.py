from django.contrib import admin
from .models import Question_designer

# Register your models here.

@admin.register(Question_designer)
class Question_designerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone')