# apps/ministries/models.py
from django.db import models
from django.utils.text import slugify


class Ministry(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ministerio")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name="Descripción")
    leader = models.CharField(max_length=100, verbose_name="Líder")
    leader_photo = models.ImageField(
        upload_to="ministries/leaders/", blank=True, null=True
    )
    image = models.ImageField(upload_to="ministries/", blank=True, null=True)
    icon_class = models.CharField(
        max_length=50, default="fa-heart", help_text="Clase de FontAwesome"
    )
    # Campos opcionales
    meeting_time = models.CharField(
        max_length=100, blank=True, verbose_name="Horario (opcional)"
    )
    meeting_location = models.CharField(
        max_length=200, blank=True, verbose_name="Lugar (opcional)"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
