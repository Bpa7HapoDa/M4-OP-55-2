from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm, PostModelForm
from .models import Post

def text_response_view(request):
    return HttpResponse("Текст")

def html_template_view(request):
    context = {
        'title': 'Привет!',
        'message': 'Текст!',
    }
    return render(request, 'myapp/template.html', context)

def create_post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                image=form.cleaned_data.get('image')
            )
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'myapp/create_post.html', {'form': form})

def create_post_modelform(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm()
    return render(request, 'myapp/create_post.html', {'form': form})

from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'myapp/post_list.html'
    context_object_name = 'posts'
