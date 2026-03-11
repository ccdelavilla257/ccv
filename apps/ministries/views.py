from django.shortcuts import render, get_object_or_404
from .models import Ministry


def ministry_list(request):
    ministries = Ministry.objects.all()
    return render(request, "ministries/list.html", {"ministries": ministries})


def ministry_detail(request, slug):
    ministry = get_object_or_404(Ministry, slug=slug)
    return render(request, "ministries/detail.html", {"ministry": ministry})
