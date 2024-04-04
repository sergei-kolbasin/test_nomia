from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import SurveyForm
from .models import Question, Answer


class EnterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        question = Question.objects.get(id=3)
        selected_answers = Answer.objects.filter(survey__question=question)

        form = SurveyForm(instance=question)
        form.fields['answers'].queryset = selected_answers

        context = {
            'form': form,
            'question': question,
            'selected_answers': selected_answers
        }

        return render(request, 'questionnaire/enter.html', context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = SurveyForm(request.POST)
        if form.is_valid():
            selected_answer = str(form.cleaned_data['answers'][0].text)
            if selected_answer == 'Создайте первое заведение':
                return render(request, 'questionnaire/create_institution.html')
            elif selected_answer == 'Зайти в личный кабинет':
                return redirect((reverse('questionnaire:account')))

        return render(request, 'questionnaire/account.html')


class CreateInstitution(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'questionnaire/create_institution.html')


class Accaunt(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'user': User.objects.get(id=1)
        }
        return render(request, 'questionnaire/account.html', context=context)
