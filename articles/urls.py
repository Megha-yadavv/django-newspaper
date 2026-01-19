from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articleView, name='article'),
    path('article_list/', views.articleList, name='article_list'),
     path('article_edit/<int:id>/', views.articleEdit, name='article_edit'),
     path('article_delete/<int:id>/', views.articleDelete, name='article_delete')
]
