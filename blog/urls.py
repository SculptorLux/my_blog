from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts_info),
    path('<int:number_post>', views.personal_post_number),
    path('<str:name_post>', views.personal_post),
]