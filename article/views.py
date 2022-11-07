from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from article.forms import CreateArticleForm
from article.models import Article
from locator_coffeeshop import settings
from user.models import Profile


def get_base_data(request):

    data = {
        'main_menu': settings.MAIN_MENU,
        'user_data': Profile.manager.get_user_by_id(request.user.id)
    }

    return data


@method_decorator(login_required, name='dispatch')
class ArticlesList(ListView):
    template_name = 'article/article_list.html'
    model = Article

    def get_context_data(self, *, object_list=None, **kwargs):

        data = super().get_context_data(**kwargs)
        data['articles'] = Article.manager.get_articles()
        data.update(get_base_data(self.request))

        return data

    def post(self, request, *args, **kwargs):
        pass


@method_decorator(login_required, name='dispatch')
class CreateArticleView(CreateView):
    template_name = 'article/create_article.html'
    model = Article
    form_class = CreateArticleForm

    def get_context_data(self, **kwargs):

        data = super().get_context_data(**kwargs)
        data.update(get_base_data(self.request))
        data['article'] = CreateArticleForm()

        return data
