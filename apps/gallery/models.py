from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=100, verbose_name="Álbum")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="images", null=True, blank=True
    )
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="gallery/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, verbose_name="Destacar en inicio")

    class Meta:
        ordering = ["-uploaded_at"]
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"

    def __str__(self):
        return self.title or f"Imagen {self.id}"
