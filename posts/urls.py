from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.PostListView.as_view(), name="index"),
    path("create/", views.PostCreateView.as_view(), name='create_post'),
    path("update/<int:pk>", views.PostUpdateView.as_view(), name='update_post'),
    path("group/<slug:slug>/", views.group_posts, name="group_posts"),
    path("new/", views.new_post, name="new_post"),
]