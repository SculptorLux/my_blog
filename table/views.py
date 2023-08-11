from django.shortcuts import render


def table_func(request):
    return render(request, 'table/new_shablon_with_static.html')