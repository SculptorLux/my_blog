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
    context = {
        'name': name_post
    }
    return render(request, 'blog/detail_by_name.html', context)


def personal_post_number(request, number_post: int):
    context = {
        'number': number_post,
    }
    return render(request, 'blog/detail_by_number.html', context)


def keanu(request):
    context = {
        'year_born': '2 сентября 1964 г.',
        'city_born': 'Бейрут',
        'movie_name': 'Джон Уик',
    }
    return render(request, 'blog/keanu.html', context)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinnessworldrecords.html', context)
