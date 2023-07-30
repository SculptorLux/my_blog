from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.posts_info),
    path('', views.main),
    path('posts/<name_post>', views.personal_post),
]