from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Profile, Trivia, Question

""" Test cases for API Endpoints"""
class TestCases(APITestCase):
    def setUp(self):
        print('------------setting up auth and user-------------\n')
        self.client = APIClient()
        """ create user and obtain auth token """
        self.data = (
            {"username": "jackson", "password": "secret", "email": "jackson@beatles.com"}
        )
        self.trivia_data = (
            {"title": "test_fun_time", "category": "1", "type": "2"}
        )
        self.user = get_user_model().objects.create_user(**self.data)
        self.user.raw_password = self.data["password"]
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)


    def test_create_user_has_profile(self):
        """ test that creating a user creates a profile with an empty score """
        url = '/api/v1/profile/1/'
        response = self.client.get(url, format='json')

        print('------------created user has profile--------------\n')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.get().score, 0)


    def test_create_trivia(self):
        """ test trivia creation  """
        url = '/api/v1/trivia/'
        response = self.client.post(
            url,
            self.trivia_data,
            format='json'
        )

        print('------------create trivia-------------------------\n')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Trivia.objects.count(), 1)
        self.assertEqual(Trivia.objects.get().title, 'test_fun_time')


    def test_create_questions(self):
        url = '/api/v1/trivia/1/questions/'
        data = {"content": "This is a test?", "correct": "yes it is", "inccorect": "no it isnt", "category": "1", "type": "2"}
        response = self.client.post(
            url,
            data,
            format='json'
        )

        print('------------create question---------------------\n')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(Question.objects.get().content, 'This is a test?')
