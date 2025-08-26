from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('text/', views.text_response_view, name='text_response'),
    path('html/', views.html_template_view, name='html_template'),
    path('posts/new-form/', views.create_post_form, name='create_post_form'),
    path('posts/new-modelform/', views.create_post_modelform, name='create_post_modelform'),
    path('posts/', PostListView.as_view(), name='post_list')
]
