from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('create/', views.create_post, name='create_post'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('<int:post_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comment_delete'),
]