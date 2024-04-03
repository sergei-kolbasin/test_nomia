from django.contrib import admin

from .models import Question, Answer, Institution, Survey


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ["name", "city_country", "address", "business_type", "direction", "service_type"]
    list_display_links = ["name", "city_country", "address", "business_type", "direction", "service_type"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "comment",]
    list_display_links = ["title", "comment"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["text"]
    list_display_links = ["text"]


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ["question", "display_answers"]
    list_display_links = ["question", "display_answers"]

    def display_answers(self, obj):
        return ", ".join([answer.text for answer in obj.answers.all()])

    display_answers.short_description = 'Answers'
