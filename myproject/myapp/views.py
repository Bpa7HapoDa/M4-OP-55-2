from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

def text_response_view(request):
    return HttpResponse("Текст")

def html_template_view(request):
    context = {
        'title': 'Привет!',
        'message': 'Текст!',
    }
    return render(request, 'myapp/template.html', context)

from .models import Post
from django.conf import settings

def list_view(request):
    posts = Post.objects.select_related('category').prefetch_related('tags').order_by('-created_at')
    return render(request, 'myapp/post_list.html', {'posts': posts})
