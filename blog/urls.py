from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.posts_info),
    path('', views.main),
    path('posts/<int:number_post>', views.personal_post_number),
    path('posts/<str:name_post>', views.personal_post),
]