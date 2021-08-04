from django.urls import path, include
from .views import (
    BlogUserViewset,
    PostViewset,
    CommentViewset,
    AlbumViewset,
    PhotoViewset,
    TodoViewset,
    ConsultPlaceholderServices
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', BlogUserViewset)
router.register('posts', PostViewset)
router.register('comments', CommentViewset)
router.register('albums', AlbumViewset)
router.register('photos', PhotoViewset)
router.register('todos', TodoViewset)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/consult/', ConsultPlaceholderServices),
]
