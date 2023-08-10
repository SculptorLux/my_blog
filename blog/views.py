from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def posts_info(request):
    return HttpResponse("Все посты блога")


def main(request):
    return HttpResponse("Главная страница")


def personal_post(request, name_post):
    return HttpResponse(f"Информация о посте {name_post}")


def personal_post_number(request, number_post: int):
    return HttpResponse(f"Здесь содержится информация о посте под номером {number_post}")