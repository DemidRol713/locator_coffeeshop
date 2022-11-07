from django.db import models
from django.utils import timezone

from article.article_manager import ArticleManager


class Article(models.Model):

    name = models.CharField(reversed, max_length=200)
    article = models.TextField()
    author = models.CharField(max_length=50)
    date_created = models.DateField(default=timezone.now)

    manager = ArticleManager()