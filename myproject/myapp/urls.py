from django.urls import path
from . import views  # Правильный импорт вьюшек

urlpatterns = [
    path('text/', views.text_response_view, name='text_response'),
    path('html/', views.html_template_view, name='html_template'),
]