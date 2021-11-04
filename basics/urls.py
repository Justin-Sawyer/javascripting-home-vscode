from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.all_basics, name='basics'),
    path('<int:article_id>/', views.article, name='article_detail'),
    path('add/', views.add_article, name='add_article'),
    path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
]
