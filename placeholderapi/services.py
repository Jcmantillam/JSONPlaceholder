import requests
import json
from decouple import config
from typing import List, Set, Dict, Tuple, Optional
from .constants import (
    PACEHOLDER_USER_BY_ID,
    PACEHOLDER_POSTS_BY_ID,
    PACEHOLDER_COMMENT_BY_ID,
    PACEHOLDER_ALBUM_BY_ID,
    API_USER,
    API_POST,
    API_COMMENT
)
from .models import BlogUser, Post, Comment, Album, Photo, Todo
from .utils import API_requests, identify_object

#Consulting JSONPlaceholder resources
'''
 Gets user giving the IdUser
    params: id:int
    returns: Dict
'''
def consult_user(id: int) -> Dict:
    url = config('EXTERNAL_API') + PACEHOLDER_USER_BY_ID.format(id=id)
    headers = {}
    data = {}
    response = API_requests(url, "GET", headers, data)
    return response


'''
 Gets a post giving the PostId
    params: id:int
    returns: Dict
'''
def consult_post(id: int) -> Dict:
    url = config('EXTERNAL_API') + PACEHOLDER_POSTS_BY_ID.format(id=id)
    headers = {}
    data = {}
    response = API_requests(url, "GET", headers, data)
    return response


'''
 Gets a comment giving the Id
    params: id:int
    returns: Dict
'''
def consult_comment(id: int) -> Dict:
    url = config('EXTERNAL_API') + PACEHOLDER_COMMENT_BY_ID.format(id=id)
    headers = {}
    data = {}
    response = API_requests(url, "GET", headers, data)
    return response


'''
 Gets an album giving the Id
    params: id:int
    returns: Dict
'''
def consult_album(id: int) -> Dict:
    url = config('EXTERNAL_API') + PACEHOLDER_ALBUM_BY_ID.format(id=id)
    headers = {}
    data = {}
    response = API_requests(url, "GET", headers, data)
    return response


'''
Consumes the service given on the request, if save_result
is False, returns just the data from the rquest; Else verify
the objects and saves the information and the related objects
    params: data:Dict
    returns: Dict
'''
def consult_process(data: Dict) -> Dict:
    url = config('EXTERNAL_API') + data['service']
    response = API_requests(url, "GET", {}, {})
    content = response.json()

    if not data['save_result']:
        return content
    
    if isinstance(content, list):
        if len(content) == 0:
            return content
        object_type = identify_object(data=content[0])
        for obj in content:
            verify_and_save(
                object=obj,
                object_type=object_type
            )
    else:
        object_type = identify_object(data=content)
        verify_and_save(
            object=content,
            object_type=object_type
        )

    return content


'''
Givven a object(dictionary), and a type, verifys if the
object is saved in the local BD. If the object does not
exist in local BD, then it is saved.
    params: object:Dict, object_type:str
    returns: None
'''
def verify_and_save(object: Dict, object_type: str) -> None:
    if object_type == 'user':
        user = BlogUser.objects.filter(username=object['username'])
        if user:
            return

        BlogUser.objects.create(
            name=object['name'],
            username=object['username'],
            email=object['email'],
            address=object['address'],
            phone=object['phone'],
            website=object['website'],
            company=object['company']
        )
    elif object_type == 'post':
        user_id = object['userId']
        user_obj = consult_user(id=user_id).json()

        verify_and_save(
            object=user_obj,
            object_type='user'
        )
        
        user = BlogUser.objects.filter(username=user_obj['username'])
        post = Post.objects.filter(
            blog_user=user.first(),
            title=object['title'],
            body=object['body']
        )

        if post:
            return

        Post.objects.create(
            blog_user=user.first(),
            title=object['title'],
            body=object['body']
        )

    elif object_type == 'comment':
        post_id = object['postId']
        post_obj = consult_post(id=post_id).json()
        user_id = post_obj['userId']
        user_obj = consult_user(id=user_id).json()

        verify_and_save(
            object=post_obj,
            object_type='post'
        )

        user = BlogUser.objects.filter(username=user_obj['username'])
        post = Post.objects.filter(
            blog_user=user.first(),
            title=post_obj['title'],
            body=post_obj['body']
        )

        comment = Comment.objects.filter(
            name=object['name'],
            post=post.first(),
            email=object['email'],
            body=object['body']
        )
        if comment:
            return

        Comment.objects.create(
            name=object['name'],
            post=post.first(),
            email=object['email'],
            body=object['body']
        )

    elif object_type == 'album':
        user_id = object['userId']
        user_obj = consult_user(id=user_id).json()

        verify_and_save(
            object=user_obj,
            object_type='user'
        )

        user = BlogUser.objects.filter(username=user_obj['username'])

        album = Album.objects.filter(
            title=object['title'],
            user=user.first()
        )
        if album:
            return
        

        Album.objects.create(
            title=object['title'],
            user=user.first()
        )
    elif object_type == 'photo':
        album_id = object['albumId']
        album_obj = consult_album(id=album_id).json()

        verify_and_save(
            object=album_obj,
            object_type='album'
        )

        user_obj = consult_user(id=album_obj['userId']).json()
        user = BlogUser.objects.filter(username=user_obj['username'])
        album = Album.objects.filter(
            title=album_obj['title'],
            user=user.first()
        )
        photo = Photo.objects.filter(
            title=object['title'],
            album=album.first(),
            url=object['url'],
            thumbnailUrl=object['thumbnailUrl']
        )

        if photo:
            return

        photo = Photo.objects.create(
            title=object['title'],
            album=album.first(),
            url=object['url'],
            thumbnailUrl=object['thumbnailUrl']
        )
    elif object_type == 'todo':
        user_id = object['userId']
        user_obj = consult_user(id=user_id).json()

        verify_and_save(
            object=user_obj,
            object_type='user'
        )
        #import pdb; pdb.set_trace()
        user = BlogUser.objects.filter(username=user_obj['username'])
        todo = Todo.objects.filter(
            title=object['title'],
            completed=object['completed'],
            user=user.first()
        )

        if todo:
            return

        todo = Todo.objects.create(
            title=object['title'],
            completed=object['completed'],
            user=user.first()
        )
