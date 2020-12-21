
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("edit_post", views.edit_post, name="edit_post"),
    path("profile/<username>", views.profileview, name="profileview"),
    path("following", views.following, name="following"),
    path("follow_user", views.follow_user, name="follow_user"),
    path("like_post", views.like_post, name="like_post"),
    
        # API Routes
    path("all_posts", views.all_posts, name="all_posts"),
    path("all_posts_edit/<int:id>", views.all_posts_edit, name="all_posts_edit"),
    path("user_followed", views.user_followed, name="user_followed"),
]

