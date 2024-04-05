from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Question


class TestEnterView(TestCase):
    def setUp(self):
        Question.objects.create(title='Что вы хотите сделать?')

    def test_EnterView(self):
        response = self.client.get(reverse('questionnaire:enter'))
        content = response.content.decode('utf-8')
        self.assertInHTML('Что вы хотите сделать?', content)  # проверка на наличие данной фразы на сайте
        self.assertEqual(response.status_code, 200)  # проверка на статус код
        self.assertTemplateUsed(response, 'questionnaire/enter.html')  # проверка на использование конкретного шаблона
        # проверка на наличие в контексе определнных переменных
        self.assertIn('form', response.context)
        self.assertIn('question', response.context)


class TestCreateInstitutionView(TestCase):
    def setUp(self):
        Question.objects.create(title='Создайте первое заведение')

    def test_CreateInstitutionView(self):
        response = self.client.get(reverse('questionnaire:create_institution'))
        content = response.content.decode('utf-8')
        self.assertInHTML('Создайте первое заведение', content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/create_institution.html')
        self.assertIn('form', response.context)
        self.assertIn('question', response.context)


class TestAccountView(TestCase):
    def setUp(self):
        User.objects.create(username='sergei', password='123')

    def test_AccountView(self):
        response = self.client.get(reverse('questionnaire:account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/account.html')
        self.assertIn('user', response.context)


class TestBusinessTypeView(TestCase):
    def setUp(self):
        Question.objects.create(title='Какой у Вас тип бизнеса?')

    def test_CreateInstitutionView(self):
        response = self.client.get(reverse('questionnaire:business_type'))
        content = response.content.decode('utf-8')
        self.assertInHTML('Какой у Вас тип бизнеса?', content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/business_type.html')
        self.assertIn('form', response.context)
        self.assertIn('question', response.context)


class TestCateringView(TestCase):
    def setUp(self):
        Question.objects.create(title='Каким типом заведения вы владеете:')

    def test_CreateInstitutionView(self):
        response = self.client.get(reverse('questionnaire:catering'))
        content = response.content.decode('utf-8')
        self.assertInHTML('Каким типом заведения вы владеете:', content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/catering.html')
        self.assertIn('form', response.context)
        self.assertIn('question', response.context)


class TestCateringTypeView(TestCase):
    def setUp(self):
        Question.objects.create(title='Какие типы сервисов вы будете предоставлять в вашем заведении?')

    def test_CreateInstitutionView(self):
        response = self.client.get(reverse('questionnaire:catering_type'))
        content = response.content.decode('utf-8')
        self.assertInHTML('Какие типы сервисов вы будете предоставлять в вашем заведении?', content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/catering_type.html')
        self.assertIn('form', response.context)
        self.assertIn('question', response.context)


class TestRetailView(TestCase):
    def setUp(self):
        Question.objects.create(title='Выберите тип ритейла')

    def test_CreateInstitutionView(self):
        response = self.client.get(reverse('questionnaire:retail'))
        content = response.content.decode('utf-8')
        self.assertInHTML('Выберите тип ритейла', content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/retail.html')
        self.assertIn('form', response.context)
        self.assertIn('question', response.context)


class TestRetailTypeView(TestCase):
    def setUp(self):
        Question.objects.create(title='Какой вид заказов?')

    def test_CreateInstitutionView(self):
        response = self.client.get(reverse('questionnaire:retail_type'))
        content = response.content.decode('utf-8')
        self.assertInHTML('Какой вид заказов?', content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/retail_type.html')
        self.assertIn('form', response.context)
        self.assertIn('question', response.context)


class TestServiceTypeView(TestCase):
    def setUp(self):
        Question.objects.create(title='Какие услуги оказывает Ваше заведение:')

    def test_CreateInstitutionView(self):
        response = self.client.get(reverse('questionnaire:services_type'))
        content = response.content.decode('utf-8')
        self.assertInHTML('Какие услуги оказывает Ваше заведение:', content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionnaire/services_type.html')
        self.assertIn('form', response.context)
        self.assertIn('question', response.context)

