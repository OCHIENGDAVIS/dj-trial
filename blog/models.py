from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title of the Book')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.user


class Tag(models.Model):
    tag_name = models.CharField(max_length=120)
    blog_posts = models.ManyToManyField(BlogPost)

    def __str__(self):
        return self.tag_name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    body = models.CharField(max_length=500, verbose_name='Your Comment')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body[:50]
