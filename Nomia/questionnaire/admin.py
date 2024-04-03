from django.contrib import admin

from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "comment", "display_answers"]
    list_display_links = ["title", "comment"]

    def display_answers(self, obj):
        return ", ".join([answer.text for answer in obj.answers.all()])

    display_answers.short_description = 'Answers'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["text"]
    list_display_links = ["text"]
