from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts_info),
    path('keanu', views.keanu),
    path('guinness_world_records', views.get_guinness_world_records),
    path('<int:number_post>', views.personal_post_number),
    path('<str:name_post>', views.personal_post),
]