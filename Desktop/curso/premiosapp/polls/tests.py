import datetime
from django.test import TestCase
from django.utils import timezone
from premiosapp.polls.models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text = "¿Quien es el mejor Course director de Platzi?", pub_date =time)
        self.assertIs(future_question.was_published_recently(), False)

