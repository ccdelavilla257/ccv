from django.contrib import admin
from .models import Album, GalleryImage


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3
    fields = ["title", "image", "is_featured"]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "image_count"]
    inlines = [GalleryImageInline]

    def image_count(self, obj):
        return obj.images.count()

    image_count.short_description = "Cantidad de imágenes"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ["title", "album", "uploaded_at", "is_featured"]
    list_filter = ["album", "is_featured"]
    list_editable = ["is_featured"]
    search_fields = ["title"]
    date_hierarchy = "uploaded_at"
