from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def posts_info(request):
    return HttpResponse("Все посты блога")


def main(request):
    return HttpResponse("Главная страница")


def personal_post(request, name_post):
    return HttpResponse(f'Информация о посте {name_post}')