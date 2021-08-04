from django.test import TestCase

import json

from rest_framework.test import APIClient
from rest_framework import status

from placeholderapi.models import BlogUser, Album, Photo
from placeholderapi.constants import API_PHOTO

from decouple import config

class PhotoTestCase(TestCase):

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

        Album.objects.create(
            title="title",
            user=user
        )


    def test_create_photo(self):
        client = APIClient()

        album = Album.objects.all()
        test_photo_data = {
            "title": "Foto",
            "url": "https://via.placeholder.com/600/92c952",
            "thumbnailUrl": "https://via.placeholder.com/150/771796",
            "album": album.first().id
        }

        service = config('HOSTING') + API_PHOTO
        response = client.post(
            service, 
            test_photo_data,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('title', result)


        if 'id' in result:
            del result['id']

        self.assertEqual(result, test_photo_data)


    def test_get_album(self):

        client = APIClient()

        album = Album.objects.all()
        Photo.objects.create(
            title="Foto",
            url="https://via.placeholder.com/600/92c952",
            thumbnailUrl="https://via.placeholder.com/150/771796",
            album=album.first()
        )

        service = config('HOSTING') + API_PHOTO
        response = client.get(service)
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)


    def test_delete_album(self):

        client = APIClient()

        album = Album.objects.all()
        photo = Photo.objects.create(
            title="Foto",
            url="https://via.placeholder.com/600/92c952",
            thumbnailUrl="https://via.placeholder.com/150/771796",
            album=album.first()
        )

        service = config('HOSTING') + API_PHOTO + f'{photo.id}/'
        response = client.delete(
            service, 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        photo_exists = Photo.objects.filter(pk=photo.id)
        self.assertFalse(photo_exists)
