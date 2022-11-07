from django.db import models


class ArticleManager(models.Manager):

    def get_articles(self):

        return super().get_queryset().all()

    def get_article_by_id(self, _id):

        return super().get_queryset().get(_id)

    def get_articles_by_author(self, _author):

        return super().get_queryset().filter(author=_author)

    def get_articles_by_name(self, _name):

        return super().get_queryset().filter(name=_name)