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