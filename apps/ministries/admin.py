from django.contrib import admin
from .models import Ministry


@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ["name", "leader"]  # Eliminado 'order'
    search_fields = ["name", "leader", "description"]
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = (
        ("Información Principal", {"fields": ("name", "slug", "leader", "icon_class")}),
        ("Descripción", {"fields": ("description",)}),
        ("Imágenes", {"fields": ("image", "leader_photo"), "classes": ("collapse",)}),
        (
            "Información opcional",
            {"fields": ("meeting_time", "meeting_location"), "classes": ("collapse",)},
        ),
    )
