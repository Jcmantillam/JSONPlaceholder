from django.test import TestCase

import json

from rest_framework.test import APIClient
from rest_framework import status

from placeholderapi.models import BlogUser
from placeholderapi.constants import API_USER

from decouple import config

class BlogUserTestCase(TestCase):

    def test_create_user(self):
        client = APIClient()

        test_user_data = {
            "name": "name",
            "username": "cmantillam",
            "email": "email@email.com",
            "address": {},
            "phone": "11111111",
            "website": "www.web.com",
            "company": {}
        }

        service = config('HOSTING') + API_USER
        response = client.post(
            service, 
            test_user_data,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('name', result)
        self.assertIn('username', result)
        self.assertIn('email', result)
        self.assertIn('phone', result)

        if 'id' in result:
            del result['id']

        self.assertEqual(result, test_user_data)


    def test_get_user(self):

        client = APIClient()

        BlogUser.objects.create(
            name="name",
            username="cmantillam",
            email="email@email.com",
            address={},
            phone="11111111",
            website="www.web.com",
            company={}
        )

        service = config('HOSTING') + API_USER
        response = client.get(service)
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)


    def test_delete_user(self):

        client = APIClient()


        user = BlogUser.objects.create(
            name="name",
            username="cmantillam",
            email="email@email.com",
            address={},
            phone="11111111",
            website="www.web.com",
            company={}
        )

        service = config('HOSTING') + API_USER + f'{user.id}/'
        response = client.delete(
            service, 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        user_exists = BlogUser.objects.filter(pk=user.id)
        self.assertFalse(user_exists)
