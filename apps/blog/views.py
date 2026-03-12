import re
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    posts_list = Post.objects.all().order_by("-published_date")
    paginator = Paginator(posts_list, 5)  # 5 artículos por página

    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    return render(request, "blog/list.html", {"posts": posts})


def post_detail(request, pk):  # <-- CAMBIA AQUÍ (slug → pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/detail.html", {"post": post})


def blog_search(request):
    query = request.GET.get("q", "")
    resultados = []

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(excerpt__icontains=query)
        ).order_by("-published_date")

        for post in posts:
            contenido = post.content
            palabras = query.split()

            fragmentos = []
            for palabra in palabras:
                pattern = r"(.{0,50}" + re.escape(palabra) + r".{0,50})"
                matches = re.findall(pattern, contenido, re.IGNORECASE)
                for match in matches[:2]:
                    fragmento_resaltado = re.sub(
                        f"({re.escape(palabra)})",
                        r'<span class="bg-gold black pa1">\1</span>',
                        match,
                        flags=re.IGNORECASE,
                    )
                    if fragmento_resaltado not in fragmentos:
                        fragmentos.append(fragmento_resaltado)

            resultados.append({"post": post, "fragmentos": fragmentos[:3]})

    return render(
        request,
        "blog/search_results.html",
        {"resultados": resultados, "query": query, "total": len(resultados)},
    )
