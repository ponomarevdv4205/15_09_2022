import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import auth
from users.models import User
from .views import UserViewSet
from .models import Project, ToDo


class TestUserViewSet(TestCase):

    def setUp(self) -> None:
        self.url = '/api/projects/'
        self.projects = {'id': "2", 'name': 'Проект Val_1 + Пономарева_3'}
        self.projects_id = '2'
        self.projects_fake = {'id': "2", 'name': 'Проект Val_1 + Пономарева_3'}
        self.format = 'json'
        self.login = 'dima'
        self.password = '123'


    # Тестирование с помощью класса APIRequestFactory

    def test_factory_client_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url, format=self.format)
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тестирование с помощью класса APIClient

    def test_api_update_guest(self):
        client = APIClient()
        response = client.put(f'{self.url}{self.projects_id}/', **self.projects)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self) -> None:
        pass


# Тестирование с помощью APITestCase
class TestTodo(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/todo/'
        self.url2 = '/api/projects/'
        self.projects = {'id': "2", 'name': 'Проект Val_1 + Пономарева_3'}
        self.projects_id = '2'
        self.projects_fake = {'id': "2", 'name': 'Проект Val_1 + Пономарева_3'}
        self.format = 'json'
        self.login = 'dima'
        self.password = '123'

    def test_api_test_case_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_test_case_update_admin(self):
        self.client.login(username='dima', password='123')
        response = self.client.put(f'{self.url2}{self.projects_id}/', self.projects_fake)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_mixer(self):
        proj = mixer.blend(Project, link='url')
        response = self.client.get(f'{self.url2}{proj.id}/', self.projects_fake)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(proj.link, 'url')

    def tearDown(self) -> None:
        pass
