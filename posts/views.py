from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create_post.html', context)


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    select1 = post.select1_users.filter(pk=request.user.pk).exists()
    select2 = post.select2_users.filter(pk=request.user.pk).exists()
    
    if request.method == 'POST':
        answer = request.POST.get('answer')

        if answer == 'select1':
            post.select1_users.add(request.user)
            post.select2_users.remove(request.user)
        elif answer == 'select2':
            post.select1_users.remove(request.user)
            post.select2_users.add(request.user)
        elif answer == 'cancel_select1':
            post.select1_users.remove(request.user)
        elif answer == 'cancel_select2':
            post.select2_users.remove(request.user)
        
    context = {
        'post': post,
        'select1': select1,
        'select2': select2,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('posts:index')