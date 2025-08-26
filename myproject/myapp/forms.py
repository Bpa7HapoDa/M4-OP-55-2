from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    content = forms.CharField(widget=forms.Textarea, label='Содержимое')
    image = forms.ImageField(required=False, label='Картинка')

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category', 'tags']
