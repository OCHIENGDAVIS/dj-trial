from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
from django.conf import settings


class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)


class ArticleManager(models.Manager):

    def get_queryset(self):
        return ArticleQuerySet(self.model)

    def search(self, query):
        return self.get_queryset().search(query=query)


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    objects = ArticleManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


def article_presave(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title)
    print(sender, instance)


def article_post_save(sender, instance, created, *args, **Kwargs):
    print('post Save')


pre_save.connect(article_presave, Article)
post_save.connect(article_post_save, Article)
