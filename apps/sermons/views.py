from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Sermon


def sermon_list(request):
    sermons = Sermon.objects.all()
    latest_sermon = sermons.first()

    # Obtener todos los años disponibles para el filtro
    years = Sermon.objects.dates("date_preached", "year", order="DESC")

    context = {
        "sermons": sermons,
        "latest_sermon": latest_sermon,
        "years": years,
    }
    return render(request, "sermons/list.html", context)


def sermon_detail(request, pk):
    sermon = get_object_or_404(Sermon, pk=pk)
    return render(request, "sermons/detail.html", {"sermon": sermon})


def sermons_by_year(request, year):
    sermons = Sermon.objects.filter(date_preached__year=year).order_by("-date_preached")
    latest_sermon = sermons.first()
    years = Sermon.objects.dates("date_preached", "year", order="DESC")

    context = {
        "sermons": sermons,
        "latest_sermon": latest_sermon,
        "years": years,
        "current_year": year,
    }
    return render(request, "sermons/list.html", context)


def sermon_search(request):
    query = request.GET.get("q", "")
    resultados = []

    if query:
        sermons = Sermon.objects.filter(
            Q(title__icontains=query)
            | Q(speaker__icontains=query)
            | Q(bible_text__icontains=query)
            | Q(description__icontains=query)
        ).order_by("-date_preached")

        for sermon in sermons:
            resultados.append(
                {
                    "sermon": sermon,
                    "fragmentos": [
                        f"Título: {sermon.title}",
                        f"Predicador: {sermon.speaker}",
                    ],
                }
            )

    return render(
        request,
        "sermons/search_results.html",
        {"resultados": resultados, "query": query, "total": len(resultados)},
    )
