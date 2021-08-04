from django.test import TestCase

import json

from rest_framework.test import APIClient
from rest_framework import status

from placeholderapi.models import BlogUser, Todo
from placeholderapi.constants import API_TODO

from decouple import config

class TodoTestCase(TestCase):

    def setUp(self):

        user = BlogUser.objects.create(
            name="name",
            username="username",
            email="email@email.com",
            address={},
            phone="11111111",
            website="www.web.com",
            company={}
        )


    def test_create_photo(self):
        client = APIClient()

        user = BlogUser.objects.all()
        test_todo_data = {
            "title": "titles",
            "completed": False,
            "user": user.first().id
        }

        service = config('HOSTING') + API_TODO
        response = client.post(
            service, 
            test_todo_data,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('title', result)


        if 'id' in result:
            del result['id']

        self.assertEqual(result, test_todo_data)


    def test_get_todo(self):

        client = APIClient()

        user = BlogUser.objects.all()
        Todo.objects.create(
            title="titles",
            completed=False,
            user=user.first()
        )

        service = config('HOSTING') + API_TODO
        response = client.get(service)
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)


    def test_delete_todo(self):

        client = APIClient()

        user = BlogUser.objects.all()
        todo = Todo.objects.create(
            title="titles",
            completed=False,
            user=user.first()
        )

        service = config('HOSTING') + API_TODO + f'{todo.id}/'
        response = client.delete(
            service, 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        todo_exists = Todo.objects.filter(pk=todo.id)
        self.assertFalse(todo_exists)