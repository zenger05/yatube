from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context=context)


def group_posts(request, slug):
    groups = get_object_or_404(Group, slug=slug)
    posts = groups.posts.all()[:10]
    name = Group.objects.filter(slug=slug)[0]
    context = {
        'posts': posts,
        'name': name
    }
    return render(request, 'posts/group_list.html', context=context)
