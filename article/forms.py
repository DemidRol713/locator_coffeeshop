from django import forms

from article.models import Article


class CreateArticleForm(forms.Form):

    class Meta():
        model = Article
        field = ('name', 'article', 'author',)