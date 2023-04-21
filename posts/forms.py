from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'select1_content', 'select2_content')
        labels = {
            'title': '제목',
            'select1_content': '선택지 1',
            'select2_content': '선택지 2'
        }