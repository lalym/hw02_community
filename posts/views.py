from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Post, Group


# function-based VIEW
def index(request):
    latest = Post.objects.all()[:11]
    # собираем тексты постов в один, разделяя новой строкой
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


@login_required
def new_post(request):
    context = {
        'title': 'Новая запись',
        'header': 'Добавить запись',
        'button': 'Добавить'
    }

    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            my_post = form.save(commit=False)
            my_post.author = request.user
            my_post.save()
            return redirect('index')

        context['form'] = form
        return render(request, 'new.html', context)

    context['form'] = form
    return render(request, 'new.html', context)


# class-based VIEW
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return super().get_queryset()[:11]


class Mixin:
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('index')


class PostCreateView(Mixin, CreateView):
    pass


class PostUpdateView(Mixin, UpdateView):
    pass
