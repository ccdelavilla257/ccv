from django.shortcuts import render, get_object_or_404
from .models import Album, GalleryImage


def gallery_index(request):
    # Obtener todos los álbumes
    albums = Album.objects.all()
    # Obtener imágenes recientes (últimas 8)
    recent_images = GalleryImage.objects.order_by("-uploaded_at")[:8]
    # Obtener imágenes destacadas (opcional)
    featured = GalleryImage.objects.filter(is_featured=True)[:12]

    context = {
        "albums": albums,
        "recent_images": recent_images,  # NUEVA VARIABLE
        "featured": featured,
    }
    return render(request, "gallery/index.html", context)


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    images = album.images.all()
    return render(request, "gallery/album.html", {"album": album, "images": images})
