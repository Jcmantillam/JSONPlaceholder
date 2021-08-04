from django.test import TestCase

import json

from rest_framework.test import APIClient
from rest_framework import status

from placeholderapi.models import BlogUser, Post, Comment
from placeholderapi.constants import API_COMMENT

from decouple import config

class CommentTestCase(TestCase):

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

        post = Post.objects.create(
            title="This is a Post",
            body="Hello this is another post",
            blog_user=user
        )


    def test_create_comment(self):
        client = APIClient()

        post = Post.objects.all()
        test_comment_data = {
            "name": "name",
            "email": "email@email.com",
            "body": "body",
            "post": post.first().id
        }

        service = config('HOSTING') + API_COMMENT
        response = client.post(
            service, 
            test_comment_data,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('name', result)
        self.assertIn('email', result)
        self.assertIn('body', result)

        if 'id' in result:
            del result['id']

        self.assertEqual(result, test_comment_data)


    def test_get_comment(self):

        client = APIClient()

        post = Post.objects.all()
        Comment.objects.create(
            name="name",
            email="email@email.com",
            body="body",
            post=post.first()
        )

        service = config('HOSTING') + API_COMMENT
        response = client.get(service)
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)


    def test_delete_comment(self):

        client = APIClient()

        post = Post.objects.all()
        comment = Comment.objects.create(
            name="name",
            email="email@email.com",
            body="body",
            post=post.first()
        )


        service = config('HOSTING') + API_COMMENT + f'{comment.id}/'
        response = client.delete(
            service, 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        comment_exists = Comment.objects.filter(pk=comment.id)
        self.assertFalse(comment_exists)
