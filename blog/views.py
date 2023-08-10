from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string


def posts_info(request):
    return HttpResponse("Все посты блога")


def main(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def personal_post(request, name_post):
    return HttpResponse(f"Информация о посте {name_post}")


def personal_post_number(request, number_post: int):
    return HttpResponse(f"Здесь содержится информация о посте под номером {number_post}")