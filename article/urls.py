from django.urls import path

from article import views

urlpatterns = [
    path('list/', views.ArticlesList.as_view(), name='article_list'),
    path('create_article/', views.CreateArticleView.as_view(), name='create_article')
]
