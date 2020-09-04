from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    latest = Post.objects.all()[:11]
    # собираем тексты постов в один, разделяя новой строкой
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
