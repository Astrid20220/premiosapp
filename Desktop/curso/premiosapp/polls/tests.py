from audioop import reverse
import datetime
from time import time
from urllib import response
from django.test import TestCase
from django.utils import timezone
from premiosapp.polls.models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text = "¿Quien es el mejor Course director de Platzi?", pub_date =time)
        self.assertIs(future_question.was_published_recently(), False)

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexTest(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are avaible.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question(self):
        create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])



    def test_past_questions(self):
        question = create_question("Future question", days=10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="Future question", days=30)
        url =reverse("polls:details", args=(future_question.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
  
