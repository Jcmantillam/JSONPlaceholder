from django.db import models


class BlogUser(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    address = models.JSONField(default=dict)
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=300)
    company = models.JSONField(default=dict)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    blog_user = models.ForeignKey(BlogUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(BlogUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    url = models.CharField(max_length=300)
    thumbnailUrl = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField()
    user = models.ForeignKey(BlogUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
