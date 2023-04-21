from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Post, Comment
from .forms import PostForm, CommentForm

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
    comment_form = CommentForm()
    comments = post.comment_set.all()
    
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
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('posts:index')


def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment_form.save()
        return redirect('posts:detail', post.pk)
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)


def comments_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('posts:detail', post_pk)