from django.contrib import admin
from .models import Question, Choice

class ChoiseInLine(admin.StackedInline):
    model = Choise
    extra: 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [ChoiseInLine]    

admin.site.register(Question, QuestionAdmin)

