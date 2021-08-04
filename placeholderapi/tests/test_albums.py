from django.test import TestCase

import json

from rest_framework.test import APIClient
from rest_framework import status

from placeholderapi.models import BlogUser, Album
from placeholderapi.constants import API_ALBUM

from decouple import config

class AlbumTestCase(TestCase):

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


    def test_create_album(self):
        client = APIClient()

        user = BlogUser.objects.all()
        test_album_data = {
            "title": "title",
            "user": user.first().id
        }

        service = config('HOSTING') + API_ALBUM
        response = client.post(
            service, 
            test_album_data,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('title', result)


        if 'id' in result:
            del result['id']

        self.assertEqual(result, test_album_data)


    def test_get_album(self):

        client = APIClient()

        user = BlogUser.objects.all()
        Album.objects.create(
            title="title",
            user=user.first()
        )

        service = config('HOSTING') + API_ALBUM
        response = client.get(service)
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)


    def test_delete_album(self):

        client = APIClient()

        user = BlogUser.objects.all()
        album = Album.objects.create(
            title="title",
            user=user.first()
        )

        service = config('HOSTING') + API_ALBUM + f'{album.id}/'
        response = client.delete(
            service, 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        comment_exists = Album.objects.filter(pk=album.id)
        self.assertFalse(comment_exists)
