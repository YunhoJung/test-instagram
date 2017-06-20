from django.shortcuts import render, redirect

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post:post_list', context=context)  # 딕셔너리


def post_delete(request, post_pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        post.delete()
    return redirect('post:post_list')


def post_details(request):
    pass

# request.user(지금 사용하고 있는 유저)